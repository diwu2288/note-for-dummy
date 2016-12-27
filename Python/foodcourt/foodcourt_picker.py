from itertools import zip_longest
import random
food_count = [
    'Asahi',
    'Kebab',
    'India',
    'Sue Ellen or Korean',
    'Pizzaria',
    'KingTan or Holiday',
    'Japanese or Jappi',
    'Persian',
    'Amazing Thai or Pong'
]


def find_places(week_num_total, num_to_select):
    print('='*20)
    print('START')
    week = {}
    for week_num in range(1, week_num_total+1):
        print('---- WEEK %s ----' % week_num)
        # 1. Get a sub dict by checking the value of key
        sub_week = {k: v for k, v in week.items() if k < week_num}

        # 2. Use sum to combine all elements of each list as value of a dict
        # into one list
        places = set(sum(list(sub_week.values()), []))

        week_before_last = set(week.get(week_num-2, []))
        week_last = set(week.get(week_num-1, []))

        tmp_1 = sorted(list(week_last-week_before_last))
        tmp_2 = sorted(list(week_before_last-week_last))
        choose_1 = tmp_1[:num_to_select]
        choose_2 = tmp_2[:(5-num_to_select)]

        print(
            'We choose them from last week: \t\t\t %s' % (choose_1)
        )
        print(
            'We choose them from the week before last week \t %s' % (choose_2)
        )
        choose = sorted(choose_1 + choose_2)
        if len(choose) < 5:
            max_num = len(places) + 1
            # 3. Create a list with a range of int
            choose_more = list(range(max_num, max_num+(5-len(choose))))
            print(
                'We choose new places \t\t\t\t %s' % (choose_more)
            )
            choose = sorted(choose + choose_more)
        msg = '---\nThis is WEEK %s, we go to \t\t\t %s'
        print(msg % (week_num, choose))
        week[week_num] = choose
    # 4. Use union() to add elements of a list (not as one element) to a set
    places = sorted(list(places.union(choose)))
    print('*'*10 + ' PLACES ' + '*'*10)
    print(places)
    print('='*20)
    print('END')
    return week, places

week, places = find_places(week_num_total=10, num_to_select=2)
random_choose = True
if random_choose:
    random.shuffle(food_count)

# 5. pair two list with zip
# if two list are not size even, it will ignore the extra.
# but if use zip_longest, it will pair None with extra elements
food_count_mapping = dict(zip_longest(places, food_count))
print(food_count_mapping)

for w, ids in week.items():
    # 6. Get a sub dict given a list of keys
    new_list = list({k: food_count_mapping[k] for k in ids}.items())
    if random_choose:
        random.shuffle(new_list)
    format_mon = ' - Monday: \t%s (%s) \n' % (new_list[0][1], new_list[0][0])
    format_tue = ' - Tuesday: \t%s (%s) \n' % (new_list[1][1], new_list[1][0])
    format_Wedn = ' - Wednsday: \t%s (%s) \n' % (new_list[2][1], new_list[2][0])
    format_thu = ' - Thursday: \t%s (%s) \n' % (new_list[3][1], new_list[3][0])
    format_fri = ' - Friday: \t%s (%s) \n' % (new_list[4][1], new_list[4][0])
    format_Week = format_mon + format_tue + format_Wedn + format_thu + format_fri
    print('Week %s:\n%s' % (w, format_Week))
