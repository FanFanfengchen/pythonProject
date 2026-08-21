Your_test_scores = int(input(":"))
Your_exam_rankings = [6, 5, 4, 3, 2, 1]
if 1 <= Your_test_scores <= 6:
    print(f'位于{Your_exam_rankings[Your_test_scores-1]}')
else:
    print('错了，也没了...')
