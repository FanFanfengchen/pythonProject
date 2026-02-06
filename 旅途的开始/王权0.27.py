import sys
import time

# 全局变量
task_completed = False


def print_speak(text):
    """逐字打印文本，模拟说话效果"""
    for char in text:
        print(char, flush=True, end='')
        time.sleep(0.27)
    print()


def print_speak_method(text, delay):
    """打印文本并添加延迟"""
    print_speak(text)
    time.sleep(delay)


def sensory_effect(effect_type):
    """添加感观元素"""
    if effect_type == "sound":
        print("🔊 [音效] 轻微的嗡鸣声在耳边响起...")
    elif effect_type == "vision":
        print("✨ [视觉] 周围的光线似乎变得柔和起来...")
    elif effect_type == "touch":
        print("🌡️ [触觉] 一股温暖的能量流过全身...")
    elif effect_type == "emotion":
        print("💭 [情感] 一种熟悉而陌生的感觉涌上心头...")
    time.sleep(0.5)


def get_user_input(prompt=""):
    """获取用户输入，处理空输入"""
    if prompt:
        print_speak(prompt)
    
    while True:
        user_input = input().strip()
        if user_input:
            return user_input
        # 空输入时继续循环


def toss():
    """处理硬币抛掷场景"""
    time.sleep(0.8)
    print_speak_method("你向上抛掷了一枚硬币，这枚硬币飞至空中", 0.75)
    print_speak_method("然后反向落入水中", 0.75)
    print_speak_method("产生涟漪", 0.7)
    print_speak_method("共振", 0.7)
    print_speak_method("扩散", 0.7)
    print_speak_method("交错", 0.7)
    print_speak_method("这便是意识与意识的交互", 1.3)
    print_speak_method("物质世界的背面", 1.3)
    print_speak_method("灵界的存在想象", 1.3)
    print_speak_method("这里是迪拉克之海", 2)
    # 原剧情灵界层级描述
    print_speak_method("灵界的深度分为数个层级，照光层，弱光层，无光层，深渊层，莫霍层，古登堡层，地心层。", 3)
    print_speak_method("正常人的梦境处于照光层，和现实有所映照；一旦进入弱光层，就多少会获得一些能力，最常见的是能看见某些东西，以及获得少部分灵力。", 4)
    print_speak_method("无光层的深度对常人而言，是足以致命的，这个级别的深度，往往寄宿着很多非人之物常人魂魄一旦进入无光层，就有被鬼神入侵的危险；深渊层，更加致命的深度，该领域长期徘徊某些精神构造体，譬如说‘魔鬼’，譬如说‘监视者’，瀛洲数量众多的鬼神，神州的神话古物，皆属于该层级，他们不会轻易死去，只是被历史遗忘了。", 5)
    print_speak_method("而往后的，基本上不会有人潜入。", 1.5)
    print_speak_method("灵界无比危险，深渊之下，藏着的是无尽虚无，还是灵长类的综合意识阿赖耶，也根本无人可知。", 3)
    print_speak_method("不过，这也并不重要。", 1.5)
    print_speak_method("如今你也没能力潜入无光层以下，你也是预计到了这个情况，所以留下的坐标锚点，位于弱光层，好处是容易找得到，坏处嘛……", 4)
    print_speak_method("待会儿就知道了。", 1.5)
    print_speak_method("前世你在灵界中打下了三个锚点，两个在弱光层，一个在无光层。", 2.5)


def anchor_point():
    """处理锚点场景"""
    time.sleep(1.3)
    print_speak_method("你选中了最近距离的一处锚点", 1.8)
    print_speak_method("意识开始潜入，如同投入水面，能感受到水压正在一步步强化。", 3)
    print_speak_method("对自身的灵魂强度，你有充足自信，不用停顿，一口气潜入水下。", 3)
    print_speak_method("搜寻，定位。", 1.5)
    print_speak_method("以太海中风平浪静，弱光层浅海，安静悬浮着一枚被定格的锚点。", 3)
    print_speak_method("它看上去平平无奇，如同一块废弃的钢铁块，根本不会有谁注意到。", 3)
    print_speak_method("锚点本身并不重要，重要的是它能连接上什么。", 2)
    print_speak_method("指尖触碰锚点，你五指攥紧，哪怕不再有用黄金瞳的绝对武力，你也是那位帝王。", 3)
    print_speak_method("三道锚点。", 1.5)
    print_speak_method("第一道是留给自己的；第二道是黑色蔷薇会的后门；第三道……", 2.5)
    print_speak_method("第一道锚点，它藏匿的是一道残留的权能碎片。", 2.5)


def bend_your_knees():
    """处理屈膝验证成功场景"""
    time.sleep(0.3)
    print_speak_method("验证通过", 0.85)
    print_speak_method("恭迎您，陛下", 3.2)
    print_speak_method("听到这句语音，你不仅不伤感，反而没心没肺的笑起来。", 2)
    print_speak_method("'得了吧，朕的帝国早亡了。'", 1.5)
    print_speak_method("浅笑间，藏着一丝怀念的意味。", 1.5)
    print_speak_method("因为录入了这句话的人……是夏绿蒂。", 2)
    print_speak_method("是陪伴了你最长久的那位灰发女巫。", 2)
    print_speak_method("可五百年岁月流转而过，没人能抵得过岁月的磨损。", 2.5)
    print_speak_method("留在这里的不过是一件死物，一件保险。", 2)
    print_speak_method("为了防止自己没死成而做了一道保险，给自己留下了一点帝王时代的老本，方便之后直接冲去教国找教皇玩摔角，一命换一伤还是做得到的，尽量给同盟国拉扯一点发育时间。", 5)
    print_speak_method("只是没想到莉莉安奴这么争气，面对不死的帝王，反手一剑创世螺旋碎片当场给他扬了骨灰，于是这件临时的保险再也没派上用场，就这么一直留到了五百年后。", 5)


def baiwei():
    """处理白维验证成功场景"""
    time.sleep(0.3)
    print_speak_method("验证通过，第一阶段解锁", 2)


def black_rose():
    """处理黑色蔷薇验证成功场景"""
    time.sleep(0.3)
    print_speak_method("验证通过，第二阶段解锁", 2)
    print_speak_method("最终阶段即将展开", 1.5)
    print_speak_method("警告：启用该权能碎片将会导致灵界海洋暴动，产生多次回响，后果难以预知", 2.5)
    print_speak_method("如果执意发动权能，请通过最终验证", 2.5)


def goodbye_charlotte():
    """处理最终验证成功场景"""
    time.sleep(0.3)
    print_speak_method("最终验证结束", 1)
    print_speak_method("黄金大权，权能展开", 1.2)
    print_speak_method("灵界海洋深处，传出无垠回响。", 2.4)
    print_speak_method("声浪如同鲸歌，回荡在灵界海洋的深层。", 2.5)
    print_speak_method("现实位面之中", 1)
    print_speak_method("你睁开双眼，眼瞳深处映照出黄金色的辉煌光芒。", 3.5)
    print_speak_method("你伫立于此，却如同端坐在黄金宫殿的恢弘王座上。", 3.7)
    print_speak_method("仅有数息的时间，黄金大权在握。", 2.4)
    print_speak_method("换做其他人，光是熟悉这种力量的用法都需要很久的时间，短短几秒只能仓促的挥霍。", 4)
    print_speak_method("而对于持有者的你，运用这股力量不需要任何的额外思考，几乎化作本能。", 3.5)
    print_speak_method("你仅抬起手", 2)
    print_speak_method("啪嗒~轻轻的打了个响指", 1.8)
    print_speak_method("召唤仪式99%......中止......", 2.35)
    print_speak_method("水池中即将满溢而出的黑泥，悄无声息的在金黄色的辉光之中湮灭而去，洒落作遍地粉尘。", 3.5)
    print_speak_method("眼瞳金色光芒不复的青年轻松的叹了口气，完全没有自己浪费了足以压垮小国政权的恐怖核威慑的自觉。", 4)
    print_speak_method("他扬起唇角，将汉刀赛回衣袖里，拍了拍身上的灰尘，旋即双手抄着口袋，走出了这片阴凉的背光区。", 4.5)
    print_speak_method("来时背对阳光，离开时面朝太阳，或许是温度正好，他在午后阳光下伸了个懒腰，慵懒的打起了哈欠，像只憨态可掬的东北金渐层……而在现实世界难以察觉的灵界海洋中，正酝酿着一场浩瀚的风暴。", 5.5)


def goodbye_charlotte_badend():
    """处理最终验证失败场景"""
    time.sleep(0.3)
    print_speak_method("不对！", 1)
    print_speak_method("最终验证结束", 1.5)
    print_speak_method("深呼吸，好好回想陪您最长久的灰发女巫是谁。", 2.5)


def black_rose_badend():
    """处理黑色蔷薇验证失败场景"""
    time.sleep(0.3)
    print_speak_method("验证失败，无法启动第二阶段的权能", 2)
    print_speak_method("别让黑色蔷薇失望啊！", 3.6)
    print_speak_method("我的陛下", 2)


def baiwei_badend():
    """处理白维验证失败场景"""
    time.sleep(0.3)
    print_speak_method("验证失败，无法启动第一阶段的权能", 2)
    print_speak_method("不会看了小凡就来验证了吧？", 2.5)
    print_speak_method("看看原作再来", 2.5)


def bend_your_knees_badend():
    """处理屈膝验证失败场景"""
    time.sleep(0.3)
    print_speak_method("验证失败，你不是他", 1)


def anchor_point_badend():
    """处理锚点选择失败场景"""
    time.sleep(2)
    print_speak_method("前往你的目的地", 2)
    print_speak_method("糟了，迪拉克之海好像有点大", 2)
    print_speak_method("再找找别的锚点吧！", 1)


def toss_badend():
    """处理硬币抛掷失败场景"""
    time.sleep(1.8)
    print_speak_method("达成成就：硬币呢？", 3)
    print_speak_method("抛掷吧！不要忘记开始", 3.2)
    print_speak_method("因为，还有重要之人需要保护。", 1)


def main_game():
    """游戏主函数"""
    global task_completed
    
    # 游戏开始
    while True:
        start = input("你是否准备好了？\n").strip()
        if start == "开始吧":
            break
        else:
            print("请输入'开始吧'来开始游戏。")
    
    print_speak_method("闭上眼睛，在心底进行观想", 1)
    
    while not task_completed:
        # 硬币抛掷阶段
        print_speak("想象你的手中的一个硬币：")
        coin_action = get_user_input()
        
        if coin_action == "抛掷":
            toss()
            sensory_effect("sound")
            
            # 目标选择阶段
            while not task_completed:
                target = get_user_input("请选择你的目标：")
                
                if target == "锚点":
                    anchor_point()
                    sensory_effect("touch")
                    
                    # 身份验证阶段
                    while not task_completed:
                        auth_code = get_user_input("身份验证...\n请输入验证代码：")
                        
                        if auth_code == "屈膝吧！":
                            bend_your_knees()
                            sensory_effect("emotion")
                            
                            # 第一阶段验证
                            while not task_completed:
                                keyword1 = get_user_input("第一阶段验证...\n验证关键词：")
                                
                                if keyword1 == "白维":
                                    baiwei()
                                    sensory_effect("vision")
                                    
                                    # 第二阶段验证
                                    while not task_completed:
                                        keyword2 = get_user_input("第二阶段验证...\n验证关键词：")
                                        
                                        if keyword2 == "黑色蔷薇":
                                            black_rose()
                                            sensory_effect("sound")
                                            
                                            # 最终验证
                                            while not task_completed:
                                                final_keyword = get_user_input("最终验证...\n验证关键词：")
                                                
                                                if final_keyword == "再见了，夏绿蒂。":
                                                    goodbye_charlotte()
                                                    task_completed = True
                                                else:
                                                    goodbye_charlotte_badend()
                                        else:
                                            black_rose_badend()
                                else:
                                    baiwei_badend()
                        else:
                            bend_your_knees_badend()
                else:
                    anchor_point_badend()
        else:
            toss_badend()


def epilogue():
    """游戏结局"""
    time.sleep(2)
    print_speak("另一边...")
    
    # 不同势力的反响
    print_speak_method("回响如钟鸣，总有些人能够听得到。", 2)
    print_speak_method("京都，幕府。", 1.5)
    print_speak_method("当一个人成为了一国的掌权者时，其身上的所有色彩都会被无限淡化，被留下的特质往往只剩下权利本身。", 3.5)
    print_speak_method("特别在这个人知晓自己一举一动都会牵扯影响上亿人时，祂就更需要抹杀自己作为人的特质，留下的仅仅是为了‘幕府将军’这一名号而存在的个体。", 4.5)
    print_speak_method("幕府便是幕府，将军就是将军，世代承袭的名号，早已不需要前缀，更不需要似乎血统高贵的天皇世家的认同，血统并非最重要的条件，继子也可以继承。", 4.5)
    print_speak_method("最重要的是素质，要在战火飘摇的世道中保持小国中立谋求之道，需要的不仅是隐忍，更是能承受重压的大心脏，以及一人守国门的强大武力。", 4.5)
    print_speak_method("因而，作为两百年来樱岛幕府唯一的上位英灵，祂早在满十岁时，就注定会坐上幕府将军的位置，以最为殊胜的身份，统领天下大权，应许臣民宏图前景，每一代的将军，最为注重的便是瀛洲的安全和平稳。", 5.5)
    print_speak_method("这一代更是尤甚，祂的起丶极高，故而眼界也极高，寻常的对手都不能称之为对手。", 3.5)
    print_speak_method("试想，你执掌一国大权，手下武将文臣躬身效忠，国力蒸蒸日上，此等情况，除了隔海相望的东西两方外，对手几乎寥寥无几，可再如何寂寞，也不能出手，只能留在这天守阁里，看着不变的日升月落潮涨潮跌。", 5.5)
    print_speak_method("不爆炸的核武，才是好核武。", 2)
    print_speak_method("今日的将军也一如既往，祂有时什么事都不用做，只坐在天守阁最高层，迎接幕府上下的朝拜即可。", 4)
    print_speak_method("结束后，祂便换了个方向，面朝大海，拿起彩色的团子，慢条斯理的咬上一口，眼中静默着排遣着无聊。", 4)
    print_speak_method("这份平静本该一直持续，倏然间，有一声回响突兀的传来。", 3)
    print_speak_method("并不是很刺耳的声音，仅仅只似是音叉在耳畔微微一震，继而迅速远去。", 3)
    print_speak_method("手中的彩团子掉落在地。", 1.5)
    print_speak_method("幕府将军霍然起身，天守阁上原本晴空万里，骤然间翻滚起层层乌云，乌云深处，有赤光破空而去，如怒龙般划破云层，穿过天空，分别落向七个不同方向。", 5.5)
    print_speak_method("赤色的雷光撕裂天空，留下醒目的色彩，劈落在瀛洲其他七座不同造型的天守阁上。", 4)
    print_speak_method("天守阁的顶端，承接赤色雷霆的正是一把把造型迥异的兵刃，兵刃上刻着幕府将军的代纹。", 4)
    print_speak_method("回响声再度传来，将军走到天守阁边缘，指尖环绕赤雷，眺望远方。", 3.5)
    print_speak_method("在天守阁下方，上百人早已跪伏在地，惊惧着将军举手投足的赫然天威。", 3.5)
    print_speak_method("回响连续响了三次，随后便再无动静。", 2.5)
    print_speak_method("幕府将军却不敢放松神色，祂仍是如临大敌的面朝东方，俄顷又转向西方，长站不坐。", 4)
    
    print_speak_method("柳生霜月忽然间有些耳鸣。", 2.5)
    print_speak_method("她不太舒服的捂住耳朵，被长袖遮住的手腕上，有云纹若隐若现。", 3)
    print_speak_method("不远处，已经黯淡的樱花色光芒再度开始微微闪烁，宛若生灵呼吸。", 3)
    
    print_speak_method("明国，邵伯湖畔。", 1.5)
    print_speak_method("有名穿着素白色长裙的少女正在牧羊，忽然间的回响声穿过这片绿草如茵的丰沃草地。", 4)
    print_speak_method("她轻轻抚摸额前的鹿角，听着这声回响，不知为何，竟有些酸涩感涌来。", 3.5)
    print_speak_method("旋即止住泪水，轻轻揉了揉眼眶，少女轻轻一叹，继续牧羊。", 3)
    print_speak_method("走动之时，被长裙所遮掩的足下传来铁链拖曳的声响。", 2.5)
    
    print_speak_method("妖国。", 1.5)
    print_speak_method("佩戴玉面的大妖踮起脚尖，折下兰香花枝。", 2.5)
    print_speak_method("狐耳轻轻抖动，她附身靠在栏杆上，对着湖面下轻轻问。", 3)
    print_speak_method("'你听到了吗？'", 1.5)
    print_speak_method("湖水涌动，赤色的鳞片贴近湖面，暗金色的眼瞳睁开。", 3)
    print_speak_method("'不准去。'玉面妖摘下一片花瓣。", 2)
    print_speak_method("半截赤色拨开湖水，水浪翻滚似鱼尾弄潮。", 2.5)
    print_speak_method("'或许是陷阱。'", 1.5)
    print_speak_method("她说：'我不信明国人，更不信英灵。'", 2.5)
    print_speak_method("湖面下的赤鳞徐徐安静。", 2)
    
    print_speak_method("同盟国，血裔驻地。", 1.5)
    print_speak_method("只披上一件外衣的鲜血公匆忙奔入办公室，打开通信塔：'连线，接通首相！'", 3.5)
    print_speak_method("通信屏幕中，浮现出一张诧异的脸。", 2.5)
    print_speak_method("同盟国秘书长，尤里乌斯·炎魔正在享受着它的下午茶时光。", 3)
    print_speak_method("'夏莎部长，您不是正在公国度假？这个点还不休息？'", 2.5)
    print_speak_method("'怎么还睡得着！'血裔的执政官脸色没有半点血色，苍白着脸色，难看至极，甚至没时间遮掩自己的胸有沟壑：'我刚刚做了一场梦，我的梦境一向很准。'", 4.5)
    print_speak_method("炎魔若有所思，点头说：'于是，你梦到什么了？'", 2.5)
    print_speak_method("'我长话短说，我在梦里，看见了一双黄金瞳！'", 2.5)
    print_speak_method("'诸位，或许我们现在要面对的，不仅是教国，还有至今都并未完全消散的帝国余孽……'", 4)
    print_speak_method("'恐怕，那群自称蔷薇会的疯子们也要归来了。'", 2.5)
    print_speak_method("炎魔顿了顿：'这的确是坏消息，不过黑色蔷薇早在三百多年前就彻底停止活动了。'", 3.5)
    print_speak_method("'我还梦到了别的。'夏莎坐在椅子上，抱住膝盖：'我梦到导师了……'", 3)
    print_speak_method("炎魔推了推鼻梁上的眼镜，无奈的摇头道：'夏莎，那已经是五百多年前的事了，如果下次只是做噩梦，别给我打电话了，我怕那边冰霜巨人那边误会。'", 4.5)
    print_speak_method("'你妈的！'血裔的执政官痛骂：'你就是不信老娘！'", 2.5)
    
    print_speak_method("教国，大圣教堂，神像下。", 1.5)
    print_speak_method("一名身穿白金色长袍的女子跪在地面，她闭着双眼，眼眸上蒙着白色的布，神色既圣洁，又慈悲。", 4)
    print_speak_method("'我听到了天启。'", 1.5)
    
    print_speak_method("灵界海洋，深渊层，悬浮着漆黑的蔷薇花，本是一片黯然的它，此时悄然点亮了两瓣。", 3.5)
    
    # 剑道场馆场景
    print_speak_method("剑道场馆。", 1.75)
    print_speak_method("'哥......你刚刚去哪了？'", 1.4)
    print_speak_method("'人有三急。'", 0.95)
    print_speak_method("'可刚刚那不是厕所的方向啊。'", 1.2)
    print_speak_method("'我有说过我急的是这方面吗？'", 1)
    print_speak_method("'……'", 3)
    print_speak_method("'好了，不逗你了。'你抬手一点妹妹的额头：'我要回去了。'", 2.5)
    print_speak_method("'这就走了？'", 1.5)
    print_speak_method("'没什么好看的，反而麻烦事不少，嗯，今晚我买菜下厨，记得早点回来。'", 4.6)
    print_speak_method("'噢噢……'柳生霜月懵懂的点头，旋即喊了声：'对了哥，我……'", 3)
    print_speak_method("她突然想到刚刚感受到的奇怪记忆，望着你的背影，只觉得突然间那么的似曾相识，像是另一个人。", 3.5)
    
    response = input("（请按回车：）").strip()
    if response == "怎么了？" or response == "怎么了":
        time.sleep(0.68)
        print_speak("'怎么了？'你回头问询。")
        print_speak("'唔，路上小心。'她还是没说出口。")
    else:
        print_speak("'怎么了？'你回头问询。")
        print_speak("'唔，路上小心。'她还是没说出口。")
    
    time.sleep(1.67)
    print_speak_method("'好，那是得当心，霓虹的车是移动的穿越设备来着……'你说着闲话走远了。", 3)
    print_speak_method("……不论如何，兄长就是兄长，其他的事不是那么重要……", 3)
    print_speak_method("柳生霜月将多余思绪抛下，这时再轻轻抚摸着手腕，白皙的手腕上什么都没有，浮现的云纹也悄然消退。", 5)
    
    # 离开极东大学场景
    print_speak_method("离开极东大学的校门时，你将证件递给门口的人员。", 2.5)
    print_speak_method("这时眼角余光瞥见了一抹白色。", 1.5)
    print_speak_method("白发银眸。", 1)
    print_speak_method("明国仙家从左方迎面而来，你顷刻间顿住，俨然大受震撼，但立刻掩盖住了神色，若无其事的右转。", 4)
    print_speak_method("云无心停下脚步，看向前方人影，却因为你转身，只隐约看见一道眼熟的背影。", 3.5)
    print_speak_method("'怎么了？'旁侧的薛寒泪问了句。", 1.5)
    print_speak_method("'……没事。'她立刻收回视线：'我们得快点找到这股气息的出处。'", 2.5)
    print_speak_method("摊开的掌心赫然是江木先前触碰到某物后的衣袖。", 3)


if __name__ == "__main__":
    main_game()
    epilogue()
