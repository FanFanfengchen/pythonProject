import time
import json
import hashlib
import random
import os
from decimal import Decimal
from datetime import datetime


def clear_screen():
    """
    清屏函数，支持跨平台
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def format_currency(amount):
    """
    格式化货币值，添加适当的中文数值单位
    
    Args:
        amount (Decimal or float or int): 金额
    
    Returns:
        str: 格式化后的金额字符串
    """
    try:
        # 转换为Decimal以保持精度
        if not isinstance(amount, Decimal):
            amount = Decimal(str(amount))
        
        # 处理负数
        is_negative = amount < 0
        if is_negative:
            amount = abs(amount)
        
        # 定义单位和对应的阈值
        units = [
            (Decimal('1000000000000000000'), '兆'),
            (Decimal('100000000'), '亿'),
            (Decimal('10000'), '万'),
            (Decimal('1000'), '千'),
            (Decimal('100'), '百')
        ]
        
        # 找到合适的单位
        for threshold, unit in units:
            if amount >= threshold:
                # 计算单位前的数值
                value = amount / threshold
                # 保留两位小数
                value = round(value, 2)
                # 移除末尾的.00
                if value == int(value):
                    value = int(value)
                formatted = f"{value}{unit}"
                break
        else:
            # 没有找到合适的单位，直接格式化
            formatted = f"{amount:.2f}"
            # 移除末尾的.00
            if '.' in formatted and formatted.endswith('.00'):
                formatted = formatted[:-3]
        
        # 添加负号
        if is_negative:
            formatted = f"-{formatted}"
        
        return formatted
    except Exception as e:
        # 出错时返回原始值
        return str(amount)


class BankAccount:
    """银行账户类"""
    
    def __init__(self, account_id, password, initial_balance=0, interest_rate=0.01, compounding_frequency='monthly'):
        """
        初始化银行账户
        
        Args:
            account_id (str): 账户ID
            password (str): 账户密码
            initial_balance (float): 初始余额，默认为0
            interest_rate (float): 年利率，默认为1%
            compounding_frequency (str): 复利频率，可选值：'daily', 'monthly', 'quarterly', 'annually'，默认为'monthly'
        """
        self.account_id = account_id
        self.password_hash = self._hash_password(password)
        self.balance = Decimal(str(initial_balance))
        self.interest_rate = Decimal(str(interest_rate))
        self.compounding_frequency = compounding_frequency
        self.transaction_history = []
        self.last_interest_date = datetime.now().date()
        self.last_compounding_date = datetime.now().date()
        
        # 工作收入相关属性
        self.last_work_income = 0  # 上一次工作收入
        self.consecutive_non_work_count = 0  # 连续未工作次数
        self.salary_reset_flag = True  # 工资是否需要重置
        self.work_days = 0  # 工作天数
        self.last_work_date = datetime.now().date()  # 上一次工作日期
        self.day_ended = False  # 当天是否已经结束
    
    def _hash_password(self, password):
        """
        对密码进行哈希处理
        
        Args:
            password (str): 原始密码
            
        Returns:
            str: 哈希后的密码
        """
        return hashlib.sha256(password.encode()).hexdigest()
    
    def verify_password(self, password):
        """
        验证密码
        
        Args:
            password (str): 输入的密码
            
        Returns:
            bool: 密码是否正确
        """
        return self.password_hash == self._hash_password(password)
    
    def deposit(self, amount):
        """
        存款
        
        Args:
            amount (float): 存款金额
            
        Returns:
            bool: 存款是否成功
        """
        try:
            amount = Decimal(str(amount))
            if amount <= 0:
                print("错误：存款金额必须大于0")
                return False
            
            # 处理存款：优先抵扣欠款
            if self.balance < 0:
                # 有欠款，优先抵扣
                debt_amount = abs(self.balance)
                if amount >= debt_amount:
                    # 存款足够抵扣所有欠款
                    remaining_amount = amount - debt_amount
                    self.balance = remaining_amount
                    self._add_transaction("存款", amount, f"账户存款，抵扣欠款{format_currency(debt_amount)}元，剩余{format_currency(remaining_amount)}元")
                    print(f"存款成功！存款金额：{format_currency(amount)}元")
                    print(f"已抵扣欠款：{format_currency(debt_amount)}元")
                    print(f"剩余存款：{format_currency(remaining_amount)}元")
                    print(f"当前余额：{format_currency(self.balance)}元")
                else:
                    # 存款不足以抵扣所有欠款
                    self.balance += amount
                    self._add_transaction("存款", amount, f"账户存款，部分抵扣欠款")
                    print(f"存款成功！存款金额：{format_currency(amount)}元")
                    print(f"已部分抵扣欠款，当前欠款：{format_currency(abs(self.balance))}元")
            else:
                # 无欠款，直接增加余额
                self.balance += amount
                self._add_transaction("存款", amount, "账户存款")
                print(f"存款成功！当前余额：{format_currency(self.balance)}")
            
            return True
        except Exception as e:
            print(f"错误：{e}")
            return False
    
    def withdraw(self, amount):
        """
        取款
        
        Args:
            amount (float): 取款金额
            
        Returns:
            bool: 取款是否成功
        """
        try:
            amount = Decimal(str(amount))
            if amount <= 0:
                print("错误：取款金额必须大于0")
                return False
            
            # 允许透支，实现欠款功能
            self.balance -= amount
            
            if self.balance < 0:
                # 产生欠款
                self._add_transaction("取款", amount, f"账户取款，产生欠款{format_currency(abs(self.balance))}元")
                print(f"取款成功！取款金额：{format_currency(amount)}元")
                print(f"当前欠款：{format_currency(abs(self.balance))}元")
            else:
                # 无欠款
                self._add_transaction("取款", amount, "账户取款")
                print(f"取款成功！当前余额：{format_currency(self.balance)}")
            
            return True
        except Exception as e:
            print(f"错误：{e}")
            return False
    
    def check_balance(self):
        """
        查看余额
        """
        print(f"当前余额：{self.balance:.2f}")
    
    def calculate_interest(self):
        """
        计算并添加利息
        
        Returns:
            bool: 计算利息是否成功
        """
        try:
            # 欠款状态下暂停利息计算
            if self.balance <= 0:
                print("当前处于欠款状态，暂停利息计算")
                return False
            
            today = datetime.now().date()
            
            # 处理last_interest_date可能是未来日期的情况
            if self.last_interest_date > today:
                # 如果last_interest_date是未来日期，重置为今天
                self.last_interest_date = today
                print("利息计算日期已重置为今天")
            
            days_passed = (today - self.last_interest_date).days
            
            # 计算利息，至少计算1天
            daily_interest_rate = self.interest_rate / Decimal('365')
            interest = self.balance * daily_interest_rate * Decimal(str(max(days_passed, 1)))
            
            if interest > 0:
                self.balance += interest
                self._add_transaction("利息", interest, "账户利息计算")
                self.last_interest_date = today
                print(f"利息计算成功！已添加利息：{format_currency(interest)}，当前余额：{format_currency(self.balance)}")
                return True
            else:
                print("当前余额为0，无法计算利息")
                return False
        except Exception as e:
            print(f"错误：{e}")
            return False
    
    def check_and_compound_interest(self):
        """
        检查是否需要根据复利频率计算利息并自动添加
        
        Returns:
            bool: 是否进行了复利计算
        """
        try:
            # 欠款状态下暂停复利计算
            if self.balance <= 0:
                return False
            
            today = datetime.now().date()
            
            # 处理last_compounding_date可能是未来日期的情况
            if self.last_compounding_date > today:
                # 如果last_compounding_date是未来日期，重置为今天
                self.last_compounding_date = today
                print("复利计算日期已重置为今天")
            
            # 确定是否需要计算复利
            need_compounding = False
            
            # 根据复利频率检查是否达到复利间隔
            if self.compounding_frequency == 'daily':
                # 每日复利：每天计算一次
                need_compounding = True
            elif self.compounding_frequency == 'monthly':
                # 每月复利：检查是否是新的月份
                need_compounding = (today.year != self.last_compounding_date.year or 
                                  today.month != self.last_compounding_date.month)
            elif self.compounding_frequency == 'quarterly':
                # 每季度复利：检查是否是新的季度
                current_quarter = (today.month - 1) // 3 + 1
                last_quarter = (self.last_compounding_date.month - 1) // 3 + 1
                need_compounding = (today.year != self.last_compounding_date.year or 
                                  current_quarter != last_quarter)
            elif self.compounding_frequency == 'annually':
                # 每年复利：检查是否是新的年份
                need_compounding = today.year != self.last_compounding_date.year
            
            if need_compounding and self.balance > 0:
                # 计算复利期间的天数
                days_since_last_compounding = (today - self.last_compounding_date).days
                
                # 计算复利
                daily_interest_rate = self.interest_rate / Decimal('365')
                interest = self.balance * daily_interest_rate * Decimal(str(max(days_since_last_compounding, 1)))
                
                if interest > 0:
                    self.balance += interest
                    self._add_transaction(f"{self.compounding_frequency}复利", interest, f"{self.compounding_frequency}复利计算")
                    self.last_compounding_date = today
                    print(f"{self.compounding_frequency}复利计算成功！已添加利息：{format_currency(interest)}，当前余额：{format_currency(self.balance)}")
                    return True
            
            return False
        except Exception as e:
            print(f"错误：{e}")
            return False
    
    def _add_transaction(self, transaction_type, amount, description=""):
        """
        添加交易记录
        
        Args:
            transaction_type (str): 交易类型
            amount (Decimal): 交易金额
            description (str): 交易描述，默认为空
        """
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.transaction_history.append({
            "type": transaction_type,
            "amount": float(amount),  # 转换为float以便JSON序列化
            "balance": float(self.balance),  # 转换为float以便JSON序列化
            "timestamp": timestamp,
            "description": description
        })
    
    def print_transaction_history(self, limit=50):
        """
        打印交易记录
        
        Args:
            limit (int): 限制显示的交易记录数量，默认为50
        """
        print("\n交易记录：")
        print("-" * 80)
        print(f"{'时间':<20} {'类型':<10} {'金额':<12} {'余额':<12} {'描述':<20}")
        print("-" * 80)
        
        # 限制显示的交易记录数量
        recent_transactions = self.transaction_history[-limit:]
        
        for transaction in recent_transactions:
            description = transaction.get('description', '')[:18]
            print(f"{transaction['timestamp']:<20} {transaction['type']:<10} "
                  f"{transaction['amount']:>10.2f}  {transaction['balance']:>10.2f}  {description:<20}")
        
        if len(self.transaction_history) > limit:
            print(f"\n... 还有 {len(self.transaction_history) - limit} 条交易记录未显示 ...")
        
        print("-" * 80)
    
    def view_bills(self):
        """
        账单查看功能，支持多条件筛选和分页浏览
        """
        print("\n=== 账单查看 ===")
        print("请设置筛选条件：")
        
        # 获取筛选条件
        start_date = input("请输入开始日期（格式：YYYY-MM-DD，按回车跳过）：").strip()
        end_date = input("请输入结束日期（格式：YYYY-MM-DD，按回车跳过）：").strip()
        min_amount = input("请输入最小金额（按回车跳过）：").strip()
        max_amount = input("请输入最大金额（按回车跳过）：").strip()
        bill_type = input("请输入账单类型（按回车跳过）：").strip()
        
        clear_screen()  # 清屏
        
        # 筛选账单
        filtered_bills = self._filter_bills(start_date, end_date, min_amount, max_amount, bill_type)
        
        if not filtered_bills:
            print("没有符合条件的账单记录")
            return
        
        # 分页浏览
        self._paginate_bills(filtered_bills)
    
    def _filter_bills(self, start_date, end_date, min_amount, max_amount, bill_type):
        """
        根据条件筛选账单
        
        Args:
            start_date (str): 开始日期
            end_date (str): 结束日期
            min_amount (str): 最小金额
            max_amount (str): 最大金额
            bill_type (str): 账单类型
        
        Returns:
            list: 筛选后的账单列表
        """
        filtered = []
        
        for bill in self.transaction_history:
            # 日期筛选
            bill_date = bill['timestamp'].split()[0]
            if start_date and bill_date < start_date:
                continue
            if end_date and bill_date > end_date:
                continue
            
            # 金额筛选
            amount = bill['amount']
            if min_amount:
                try:
                    if amount < float(min_amount):
                        continue
                except ValueError:
                    pass
            if max_amount:
                try:
                    if amount > float(max_amount):
                        continue
                except ValueError:
                    pass
            
            # 类型筛选
            if bill_type and bill['type'] != bill_type:
                continue
            
            filtered.append(bill)
        
        return filtered
    
    def _paginate_bills(self, bills, page_size=10):
        """
        分页浏览账单
        
        Args:
            bills (list): 账单列表
            page_size (int): 每页显示的账单数量
        """
        total_bills = len(bills)
        total_pages = (total_bills + page_size - 1) // page_size
        
        current_page = 1
        
        while True:
            print(f"\n=== 账单浏览（第 {current_page}/{total_pages} 页）===")
            print("-" * 90)
            print(f"{'序号':<6} {'时间':<20} {'类型':<10} {'金额':<12} {'余额':<12} {'描述':<20}")
            print("-" * 90)
            
            # 计算当前页的起始和结束索引
            start_idx = (current_page - 1) * page_size
            end_idx = min(start_idx + page_size, total_bills)
            
            # 显示当前页的账单
            for i, bill in enumerate(bills[start_idx:end_idx], start=start_idx + 1):
                description = bill.get('description', '')[:18]
                print(f"{i:<6} {bill['timestamp']:<20} {bill['type']:<10} "
                      f"{bill['amount']:>10.2f}  {bill['balance']:>10.2f}  {description:<20}")
            
            print("-" * 90)
            print(f"共 {total_bills} 条账单记录")
            
            # 分页控制
            if total_pages > 1:
                print("\n分页控制：")
                print("1. 上一页")
                print("2. 下一页")
                print("3. 首页")
                print("4. 末页")
                print("5. 退出")
                
                while True:
                    choice = input("输入你的选择：").strip()
                    clear_screen()  # 清屏
                    
                    if choice == '1':
                        if current_page > 1:
                            current_page -= 1
                        else:
                            print("已经是第一页")
                        break
                    elif choice == '2':
                        if current_page < total_pages:
                            current_page += 1
                        else:
                            print("已经是最后一页")
                        break
                    elif choice == '3':
                        current_page = 1
                        break
                    elif choice == '4':
                        current_page = total_pages
                        break
                    elif choice == '5':
                        return
                    else:
                        print("错误：无效的选择，请重新输入")
            else:
                input("按回车退出...")
                return
    
    def delete_bills(self):
        """
        账单删除功能，支持批量删除和一键删除所有
        """
        print("\n=== 账单删除 ===")
        print("请选择删除方式：")
        print("1. 批量删除选中账单")
        print("2. 一键删除所有账单")
        print("3. 取消")
        
        while True:
            try:
                choice = input("输入你的选择：").strip()
                clear_screen()  # 清屏
                
                if choice == '1':
                    self._delete_selected_bills()
                    break
                elif choice == '2':
                    self._delete_all_bills()
                    break
                elif choice == '3':
                    print("删除操作已取消")
                    return
                else:
                    print("错误：无效的选择，请重新输入")
            except Exception as e:
                print(f"错误：{e}")
    
    def _delete_selected_bills(self):
        """
        批量删除选中账单
        """
        print("\n=== 批量删除账单 ===")
        print("请输入要删除的账单序号（多个序号用逗号分隔，按回车退出）：")
        
        # 显示所有账单
        self.print_transaction_history(limit=len(self.transaction_history))
        
        # 获取要删除的账单序号
        input_str = input("\n请输入要删除的账单序号：").strip()
        if not input_str:
            return
        
        clear_screen()  # 清屏
        
        # 解析输入的序号
        try:
            indices = [int(idx.strip()) - 1 for idx in input_str.split(',')]
            # 过滤无效索引
            valid_indices = [idx for idx in indices if 0 <= idx < len(self.transaction_history)]
            
            if not valid_indices:
                print("没有有效的账单序号")
                return
            
            # 显示要删除的账单
            print("\n=== 确认删除 ===")
            print("你确定要删除以下账单吗？")
            print("-" * 90)
            print(f"{'序号':<6} {'时间':<20} {'类型':<10} {'金额':<12} {'余额':<12} {'描述':<20}")
            print("-" * 90)
            
            for idx in valid_indices:
                bill = self.transaction_history[idx]
                description = bill.get('description', '')[:18]
                print(f"{idx+1:<6} {bill['timestamp']:<20} {bill['type']:<10} "
                      f"{bill['amount']:>10.2f}  {bill['balance']:>10.2f}  {description:<20}")
            
            print("-" * 90)
            print("此操作不可恢复，确定要继续吗？")
            print("1. 取消")
            print("2. 确认删除")
            
            confirm_choice = input("输入你的选择：").strip()
            clear_screen()  # 清屏
            
            if confirm_choice == '2':
                # 按降序删除，避免索引偏移
                for idx in sorted(valid_indices, reverse=True):
                    del self.transaction_history[idx]
                
                print(f"成功删除 {len(valid_indices)} 条账单记录")
            else:
                print("删除操作已取消")
                
        except ValueError:
            print("错误：无效的序号格式")
        except Exception as e:
            print(f"错误：{e}")
    
    def _delete_all_bills(self):
        """
        一键删除所有账单
        """
        print("\n=== 一键删除所有账单 ===")
        print("警告：此操作将删除所有账单记录，不可恢复！")
        print(f"当前共有 {len(self.transaction_history)} 条账单记录")
        print("你确定要继续吗？")
        print("1. 取消")
        print("2. 确认删除所有")
        
        while True:
            try:
                choice = input("输入你的选择：").strip()
                clear_screen()  # 清屏
                
                if choice == '1':
                    print("删除操作已取消")
                    return
                elif choice == '2':
                    # 清空交易记录
                    self.transaction_history.clear()
                    print("所有账单记录已被成功删除")
                    return
                else:
                    print("错误：无效的选择，请重新输入")
            except Exception as e:
                print(f"错误：{e}")
    
    def work(self):
        """
        工作收入功能
        
        Returns:
            Decimal: 工作收入金额
        """
        print("\n=== 工作 ===")
        
        # 重置连续未工作次数
        self.consecutive_non_work_count = 0
        
        # 实现工作一次算一天的逻辑
        self.work_days += 1
        print(f"📅 工作天数：{self.work_days} 天")
        
        # 工作需要一天时间，自动推进一天
        from datetime import timedelta
        self.last_work_date += timedelta(days=1)
        self.last_interest_date = self.last_work_date
        print(f"⏰  工作完成，一天已过去，当前日期：{self.last_work_date}")
        
        # 计算工作收入
        if self.salary_reset_flag or self.last_work_income == 0:
            # 首次工作或重置后，在1000至100000000范围内随机生成
            income = random.randint(1000, 100000000)
            self.salary_reset_flag = False
            print("💼 新工作周期开始，获得随机工资！")
        else:
            # 后续工作，实现上下起伏均匀的波动机制
            # 波动范围为上一次收入的5%到20%
            fluctuation_range = int(self.last_work_income * 0.05)
            if fluctuation_range < 100:
                fluctuation_range = 100  # 确保最小波动为100
            
            # 随机波动方向
            fluctuation = random.randint(-fluctuation_range, fluctuation_range)
            income = self.last_work_income + fluctuation
            
            # 确保收入不为负数
            if income < 1000:
                income = 1000
            
            print("💼 持续工作中，工资有所波动")
        
        # 记录本次收入
        self.last_work_income = income
        
        # 处理收入：优先抵扣欠款
        income_decimal = Decimal(str(income))
        if self.balance < 0:
            # 有欠款，优先抵扣
            debt_amount = abs(self.balance)
            if income_decimal >= debt_amount:
                # 收入足够抵扣所有欠款
                remaining_income = income_decimal - debt_amount
                self.balance = remaining_income
                self._add_transaction("工作收入", income_decimal, f"工作收入，抵扣欠款{format_currency(debt_amount)}元，剩余{format_currency(remaining_income)}元")
                print(f"工作收入：{format_currency(income_decimal)}元")
                print(f"已抵扣欠款：{format_currency(debt_amount)}元")
                print(f"剩余收入：{format_currency(remaining_income)}元")
            else:
                # 收入不足以抵扣所有欠款
                self.balance += income_decimal
                self._add_transaction("工作收入", income_decimal, f"工作收入，部分抵扣欠款")
                print(f"工作收入：{format_currency(income_decimal)}元")
                print(f"已部分抵扣欠款，当前欠款：{format_currency(abs(self.balance))}元")
        else:
            # 无欠款，直接增加余额
            self.balance += income_decimal
            self._add_transaction("工作收入", income_decimal, "工作收入")
            print(f"工作收入：{format_currency(income_decimal)}元")
            print(f"当前余额：{format_currency(self.balance)}元")
        
        # 工作完成后标记为一天结束
        self.day_ended = True
        return income_decimal
    
    def increment_non_work_count(self):
        """
        增加连续未工作次数，并检查是否需要重置工资
        """
        self.consecutive_non_work_count += 1
        
        # 连续三次未工作，重置工资
        if self.consecutive_non_work_count >= 3:
            self.salary_reset_flag = True
            self.consecutive_non_work_count = 0
            print("⚠️  连续三次未工作，工资已重置！")
    
    def to_dict(self):
        """
        将账户信息转换为字典，用于序列化
        
        Returns:
            dict: 账户信息字典
        """
        return {
            "account_id": self.account_id,
            "password_hash": self.password_hash,
            "balance": str(self.balance),
            "interest_rate": str(self.interest_rate),
            "compounding_frequency": self.compounding_frequency,
            "transaction_history": self.transaction_history,
            "last_interest_date": str(self.last_interest_date),
            "last_compounding_date": str(self.last_compounding_date),
            "last_work_income": self.last_work_income,
            "consecutive_non_work_count": self.consecutive_non_work_count,
            "salary_reset_flag": self.salary_reset_flag,
            "work_days": self.work_days,
            "last_work_date": str(self.last_work_date),
            "day_ended": self.day_ended
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        从字典创建账户对象，用于反序列化
        
        Args:
            data (dict): 账户信息字典
            
        Returns:
            BankAccount: 银行账户对象
        """
        # 处理可能缺少的字段
        compounding_frequency = data.get("compounding_frequency", "monthly")
        
        account = cls(
            account_id=data["account_id"],
            password="",  # 密码已经是哈希值，不需要原始密码
            initial_balance=Decimal(data["balance"]),
            interest_rate=Decimal(data["interest_rate"]),
            compounding_frequency=compounding_frequency
        )
        account.password_hash = data["password_hash"]
        account.transaction_history = data["transaction_history"]
        account.last_interest_date = datetime.strptime(data["last_interest_date"], "%Y-%m-%d").date()
        
        # 处理可能缺少的last_compounding_date字段
        if "last_compounding_date" in data:
            account.last_compounding_date = datetime.strptime(data["last_compounding_date"], "%Y-%m-%d").date()
        else:
            account.last_compounding_date = account.last_interest_date
        
        # 处理工作收入相关字段
        account.last_work_income = data.get("last_work_income", 0)
        account.consecutive_non_work_count = data.get("consecutive_non_work_count", 0)
        account.salary_reset_flag = data.get("salary_reset_flag", True)
        account.work_days = data.get("work_days", 0)
        if "last_work_date" in data:
            account.last_work_date = datetime.strptime(data["last_work_date"], "%Y-%m-%d").date()
        else:
            account.last_work_date = datetime.now().date()
        account.day_ended = data.get("day_ended", False)
        
        return account


class BankSystem:
    """银行系统类"""
    
    def __init__(self, data_file="bank_data.json", last_login_file="last_login.json"):
        """
        初始化银行系统
        
        Args:
            data_file (str): 数据文件路径
            last_login_file (str): 上次登录信息文件路径
        """
        self.data_file = data_file
        self.last_login_file = last_login_file
        self.accounts = self._load_data()
        self.current_account = None
        self.last_login_account = self._load_last_login()
    
    def _load_data(self):
        """
        从文件加载账户数据
        
        Returns:
            dict: 账户字典，键为账户ID，值为BankAccount对象
        """
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                accounts = {}
                for account_id, account_data in data.items():
                    accounts[account_id] = BankAccount.from_dict(account_data)
                return accounts
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    def _save_data(self):
        """
        保存账户数据到文件
        """
        try:
            data = {}
            for account_id, account in self.accounts.items():
                data[account_id] = account.to_dict()
            
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"错误：保存数据失败 - {e}")
            return False
    
    def _load_last_login(self):
        """
        从文件加载上次登录账号信息
        
        Returns:
            str: 上次登录的账号ID，如果没有则返回None
        """
        try:
            with open(self.last_login_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get("last_login_account")
        except (FileNotFoundError, json.JSONDecodeError):
            return None
    
    def _save_last_login(self, account_id):
        """
        保存上次登录账号信息到文件
        
        Args:
            account_id (str): 账号ID
        """
        try:
            data = {"last_login_account": account_id}
            with open(self.last_login_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"错误：保存上次登录信息失败 - {e}")
            return False
    
    def create_account(self):
        """
        创建新账户
        """
        print("\n=== 创建新账户 ===")
        
        while True:
            account_id = input("请输入账户ID：").strip()
            if not account_id:
                print("错误：账户ID不能为空")
                continue
            
            if account_id in self.accounts:
                print("错误：该账户ID已存在")
                continue
            
            break
        
        while True:
            password = input("请输入账户密码：").strip()
            if not password:
                print("错误：密码不能为空")
                continue
            
            confirm_password = input("请确认密码：").strip()
            if password != confirm_password:
                print("错误：两次输入的密码不一致")
                continue
            
            break
        
        initial_balance = 0.0
        try:
            initial_deposit = input("请输入初始存款金额（按回车跳过）：").strip()
            if initial_deposit:
                initial_balance = float(initial_deposit)
                if initial_balance < 0:
                    print("错误：初始存款金额不能为负数")
                    initial_balance = 0.0
        except ValueError:
            print("错误：无效的金额，初始存款设为0")
        
        # 创建新账户
        new_account = BankAccount(account_id, password, initial_balance)
        
        # 如果有初始存款，添加交易记录
        if initial_balance > 0:
            new_account.deposit(initial_balance)
        
        # 保存新账户
        self.accounts[account_id] = new_account
        self._save_data()
        
        print(f"\n账户创建成功！账户ID：{account_id}")
        return new_account
    
    def login(self):
        """
        登录账户
        
        Returns:
            BankAccount: 登录成功返回账户对象，失败返回None
        """
        print("\n=== 账户登录 ===")
        
        # 显示登录选项
        print("请选择登录方式：")
        print("1. 输入新账号")
        
        # 显示上次登录的账号作为选项
        if self.last_login_account and self.last_login_account in self.accounts:
            print(f"2. 登录上次账号：{self.last_login_account}")
        print("3. 返回主菜单")
        
        choice = input("输入你的选择：").strip()
        
        if choice == '1':
            account_id = input("请输入账户ID：").strip()
        elif choice == '2' and self.last_login_account and self.last_login_account in self.accounts:
            account_id = self.last_login_account
            print(f"已选择上次账号：{account_id}")
        elif choice == '3':
            return None
        else:
            print("错误：无效的选择，请重新输入")
            return self.login()
        
        if account_id not in self.accounts:
            print("错误：账户不存在")
            return None
        
        password = input("请输入密码：").strip()
        account = self.accounts[account_id]
        
        if not account.verify_password(password):
            print("错误：密码错误")
            return None
        
        # 登录成功，计算利息并检查复利
        account.calculate_interest()
        account.check_and_compound_interest()
        self._save_data()
        
        # 保存上次登录账号信息
        self._save_last_login(account_id)
        
        print(f"\n登录成功！欢迎回来，{account_id} 先生/女士")
        self.current_account = account
        return account
    
    def logout(self):
        """
        登出账户
        """
        if self.current_account:
            self._save_data()
            print(f"登出成功！再见，{self.current_account.account_id} 先生/女士")
            self.current_account = None
        else:
            print("错误：您尚未登录")
    
    def delete_account(self, account):
        """
        注销账号
        
        Args:
            account (BankAccount): 当前登录的账户
        """
        print("\n=== 注销账号 ===")
        print("警告：注销账号将永久删除您的所有数据，此操作不可恢复。")
        print("您确定要继续吗？")
        print("1. 取消")
        print("2. 确认注销")
        
        while True:
            try:
                choice = input("输入你的选择：").strip()
                clear_screen()  # 清屏
                
                if choice == '1':
                    print("注销操作已取消")
                    # 不退出循环，返回账户菜单
                    return
                elif choice == '2':
                    # 执行注销操作
                    account_id = account.account_id
                    
                    # 记录注销日志
                    self._log_deletion(account_id)
                    
                    # 从账户字典中删除账户
                    if account_id in self.accounts:
                        del self.accounts[account_id]
                        self._save_data()
                        
                    print("账号注销成功！所有数据已被永久删除。")
                    print("感谢您使用我们的银行服务，再见！")
                    
                    # 重置当前账户
                    self.current_account = None
                    return
                else:
                    print("错误：无效的选择，请重新输入")
            except Exception as e:
                print(f"错误：{e}")
    
    def _log_deletion(self, account_id):
        """
        记录账号注销日志
        
        Args:
            account_id (str): 被注销的账户ID
        """
        try:
            import socket
            
            # 获取当前时间
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            
            # 获取IP地址
            try:
                ip_address = socket.gethostbyname(socket.gethostname())
            except:
                ip_address = "未知"
            
            # 构建日志消息
            log_message = f"[{timestamp}] 账号注销: 账户ID={account_id}, IP地址={ip_address}\n"
            
            # 写入日志文件
            with open("account_deletion.log", "a", encoding="utf-8") as f:
                f.write(log_message)
                
            print(f"注销日志已记录: {log_message.strip()}")
        except Exception as e:
            print(f"错误：记录注销日志失败 - {e}")
    
    def bill_management(self, account):
        """
        账单管理功能，整合账单查看和删除功能
        
        Args:
            account (BankAccount): 当前登录的账户
        """
        print("\n=== 账单管理 ===")
        print("请选择操作：")
        print("1. 查看账单（支持筛选和分页）")
        print("2. 删除账单（支持批量删除和一键删除）")
        print("3. 取消")
        
        while True:
            try:
                choice = input("输入你的选择：").strip()
                clear_screen()  # 清屏
                
                if choice == '1':
                    account.view_bills()
                    break
                elif choice == '2':
                    account.delete_bills()
                    # 删除后保存数据
                    self._save_data()
                    break
                elif choice == '3':
                    print("账单管理操作已取消")
                    return
                else:
                    print("错误：无效的选择，请重新输入")
            except Exception as e:
                print(f"错误：{e}")
    
    def run(self):
        """
        运行银行系统
        """
        while True:
            print("\n=== 银行账户管理系统 ===")
            print("\n" + "=" * 60)
            print("请选择操作：")
            print("1. 登录账户")
            print("2. 创建新账户")
            print("3. 退出系统")
            
            # 显示上次登录的账号作为选项
            if self.last_login_account and self.last_login_account in self.accounts:
                print(f"4. 快速登录（上次账号：{self.last_login_account}")
            
            try:
                choice = input("输入你的选择：").strip()
                clear_screen()  # 清屏
                
                if choice == '1':
                    account = self.login()
                    if account:
                        self._account_menu(account)
                elif choice == '2':
                    self.create_account()
                elif choice == '3':
                    print("感谢使用银行账户管理系统，再见！")
                    break
                elif choice == '4' and self.last_login_account and self.last_login_account in self.accounts:
                    # 快速登录上次的账号
                    account_id = self.last_login_account
                    print(f"\n=== 快速登录 ===")
                    print(f"账号：{account_id}")
                    
                    password = input("请输入密码：").strip()
                    account = self.accounts[account_id]
                    
                    if account.verify_password(password):
                        # 登录成功
                        account.calculate_interest()
                        account.check_and_compound_interest()
                        self._save_data()
                        self._save_last_login(account_id)
                        
                        print(f"\n登录成功！欢迎回来，{account_id} 先生/女士")
                        self.current_account = account
                        self._account_menu(account)
                    else:
                        print("错误：密码错误")
                else:
                    print("错误：无效的选择，请重新输入")
            except Exception as e:
                print(f"错误：{e}")
            
            time.sleep(0.5)
    
    def play_dice_game(self, account):
        """
        玩骰子游戏
        
        Args:
            account (BankAccount): 当前登录的账户
        """
        print("\n=== 骰子游戏 ===")
        print("游戏规则：")
        print("1. 玩家下注一定金额")
        print("2. 摇两颗骰子，点数相加")
        print("3. 如果第一次摇出7、11或5，玩家胜")
        print("4. 如果第一次摇出2、3或12，庄家胜")
        print("5. 否则，继续摇骰子，直到摇出7（庄家胜）或第一次的点数（玩家胜）")
        
        while True:
            # 获取下注金额
            bet_amount = self._get_valid_input("请输入下注金额（按回车退出）：")
            if bet_amount is None:
                break
            
            clear_screen()  # 清屏
            
            bet_amount = Decimal(str(bet_amount))
            if bet_amount <= 0:
                print("错误：下注金额必须大于0")
                continue
            
            if bet_amount > account.balance:
                print("错误：余额不足")
                continue
            
            # 开始游戏
            print(f"\n你下注了 {bet_amount:.2f} 元")
            time.sleep(0.5)
            
            # 第一次摇骰子
            first_point = random.randrange(1, 7) + random.randrange(1, 7)
            print(f"玩家摇出了 {first_point} 点")
            time.sleep(0.5)
            
            if first_point == 7 or first_point == 11 or first_point == 5:
                print("玩家胜!")
                # 返还双倍本金（下注金额 + 下注金额）
                win_amount = bet_amount  # 利润
                account.balance += win_amount
                account._add_transaction("骰子游戏赢", win_amount, "骰子游戏胜利奖金")
                print(f"你赢了 {win_amount:.2f} 元，当前余额：{account.balance:.2f}")
                print(f"（返还双倍本金：下注 {bet_amount:.2f} 元 + 盈利 {win_amount:.2f} 元）")
            elif first_point == 2 or first_point == 3 or first_point == 12:
                print("庄家胜!")
                account.balance -= bet_amount
                account._add_transaction("骰子游戏输", bet_amount, "骰子游戏下注输掉")
                print(f"你输了 {bet_amount:.2f} 元，当前余额：{account.balance:.2f}")
            else:
                # 继续摇骰子
                print(f"目标点数：{first_point}，继续摇骰子...")
                time.sleep(0.5)
                
                while True:
                    current_point = random.randrange(1, 7) + random.randrange(1, 7)
                    print(f"玩家摇出了 {current_point} 点")
                    time.sleep(0.5)
                    
                    if current_point == 7:
                        print("庄家胜!")
                        account.balance -= bet_amount
                        account._add_transaction("骰子游戏输", bet_amount, "骰子游戏下注输掉")
                        print(f"你输了 {bet_amount:.2f} 元，当前余额：{account.balance:.2f}")
                        break
                    elif current_point == first_point:
                        print("玩家胜!")
                        # 返还双倍本金（下注金额 + 下注金额）
                        win_amount = bet_amount  # 利润
                        account.balance += win_amount
                        account._add_transaction("骰子游戏赢", win_amount, "骰子游戏胜利奖金")
                        print(f"你赢了 {win_amount:.2f} 元，当前余额：{account.balance:.2f}")
                        print(f"（返还双倍本金：下注 {bet_amount:.2f} 元 + 盈利 {win_amount:.2f} 元）")
                        break
            
            # 保存数据
            self._save_data()
            
            # 询问是否继续
            continue_game = input("是否继续游戏（y/n）：").strip().lower()
            if continue_game != 'y':
                break
    
    def skip_days(self, account):
        """
        跳过天数，快速增加利息
        
        Args:
            account (BankAccount): 当前登录的账户
        """
        print("\n=== 跳过天数 ===")
        print("请选择要跳过的天数：")
        print("1. 1天")
        print("2. 1个星期")
        print("3. 半个月")
        print("4. 1个月")
        print("5. 半年")
        print("6. 1年")
        print("7. 取消")
        
        try:
            choice = input("输入你的选择：").strip()
            clear_screen()  # 清屏
            
            days_to_skip = 0
            if choice == '1':
                days_to_skip = 1
            elif choice == '2':
                days_to_skip = 7
            elif choice == '3':
                days_to_skip = 15
            elif choice == '4':
                days_to_skip = 30
            elif choice == '5':
                days_to_skip = 180
            elif choice == '6':
                days_to_skip = 365
            elif choice == '7':
                return
            else:
                print("错误：无效的选择")
                return
            
            if days_to_skip > 0:
                # 计算并添加利息
                daily_interest_rate = account.interest_rate / Decimal('365')
                interest = account.balance * daily_interest_rate * Decimal(str(days_to_skip))
                
                if interest > 0:
                    account.balance += interest
                    account._add_transaction("跳过天数利息", interest, "跳过天数产生的利息")
                    # 更新最后利息计算日期和复利计算日期
                    from datetime import timedelta
                    account.last_interest_date += timedelta(days=days_to_skip)
                    account.last_compounding_date += timedelta(days=days_to_skip)
                    print(f"跳过 {days_to_skip} 天后，已添加利息：{interest:.2f}，当前余额：{account.balance:.2f}")
                    self._save_data()
                else:
                    print("当前余额为0，无法计算利息")
        except Exception as e:
            print(f"错误：{e}")
    
    def _account_menu(self, account):
        """
        账户操作菜单
        
        Args:
            account (BankAccount): 当前登录的账户
        """
        while True:
            # 自动计息系统：检查是否进入新的一天
            today = datetime.now().date()
            if account.day_ended and today > account.last_interest_date:
                # 进入新的一天，计算前一天的利息
                print("\n=== 自动计息 ===")
                print(f"📅  检测到新的一天：{today}")
                print(f"💵  计算 {account.last_interest_date} 的利息...")
                
                # 计算前一天的利息
                daily_interest_rate = account.interest_rate / Decimal('365')
                interest = account.balance * daily_interest_rate
                
                if interest > 0:
                    account.balance += interest
                    # 记录利息收入及计算依据
                    calculation_basis = f"余额：{format_currency(account.balance - interest)}元，日利率：{daily_interest_rate:.6f}"
                    account._add_transaction("利息", interest, f"每日利息收入，计算依据：{calculation_basis}")
                    account.last_interest_date = today
                    print(f"✅  利息计算成功！已添加利息：{format_currency(interest)}元")
                    print(f"💰  当前余额：{format_currency(account.balance)}元")
                
                # 重置当天结束标记
                account.day_ended = False
                print("=" * 80)
            
            # 每次进入菜单时检查复利
            account.check_and_compound_interest()
            
            print("\n" + "=" * 80)
            print(f"账户：{account.account_id}")
            if account.balance < 0:
                print(f"⚠️  当前状态：欠款 {format_currency(abs(account.balance))} 元")
            else:
                print(f"当前余额：{format_currency(account.balance)} 元")
            
            # 显示工作收入状态
            if account.salary_reset_flag:
                print("💼  工资状态：可获得随机工资")
            else:
                print(f"💼  工资状态：连续工作中（上次工资：{format_currency(account.last_work_income)} 元）")
            print(f"📅  工作天数：{account.work_days} 天")
            print(f"📅  最后计息日期：{account.last_interest_date}")
            print("=" * 80)
            print("请选择操作：")
            print("1. 存钱")
            print("2. 查看存款")
            print("3. 取钱")
            print("4. 查看交易记录")
            print("5. 计算利息")
            print("6. 跳过天数")
            print("7. 玩骰子游戏")
            print("8. 账单管理")
            print("9. 工作（获取收入）")
            print("10. 登出账户")
            print("11. 注销账号")
            
            try:
                choice = input("输入你的选择：").strip()
                clear_screen()  # 清屏
                
                if choice == '1':
                    amount = self._get_valid_input("请输入要存入的金额：")
                    if amount is not None:
                        account.deposit(amount)
                        self._save_data()
                    account.increment_non_work_count()
                elif choice == '2':
                    account.check_balance()
                    account.increment_non_work_count()
                elif choice == '3':
                    amount = self._get_valid_input("请输入要取出的金额：")
                    if amount is not None:
                        account.withdraw(amount)
                        self._save_data()
                    account.increment_non_work_count()
                elif choice == '4':
                    account.print_transaction_history()
                    account.increment_non_work_count()
                elif choice == '5':
                    account.calculate_interest()
                    account.check_and_compound_interest()
                    self._save_data()
                    account.increment_non_work_count()
                elif choice == '6':
                    self.skip_days(account)
                    account.increment_non_work_count()
                elif choice == '7':
                    self.play_dice_game(account)
                    account.increment_non_work_count()
                elif choice == '8':
                    self.bill_management(account)
                    account.increment_non_work_count()
                elif choice == '9':
                    account.work()
                    self._save_data()
                    # 工作选项，不增加未工作次数
                elif choice == '10':
                    self.logout()
                    break
                elif choice == '11':
                    self.delete_account(account)
                    break
                else:
                    # 不是工作选项，增加连续未工作次数
                    account.increment_non_work_count()
                    print("错误：无效的选择，请重新输入")
            except Exception as e:
                print(f"错误：{e}")
            
            time.sleep(0.5)
    
    def _get_valid_input(self, prompt):
        """
        获取有效的数字输入
        
        Args:
            prompt (str): 输入提示
            
        Returns:
            float: 有效的数字输入，失败返回None
        """
        while True:
            try:
                value = input(prompt).strip()
                if not value:
                    return None
                
                value = float(value)
                return value
            except ValueError:
                print("错误：请输入有效的数字")
                continue


def main():
    """
    主函数
    """
    bank_system = BankSystem()
    bank_system.run()


if __name__ == "__main__":
    main()
