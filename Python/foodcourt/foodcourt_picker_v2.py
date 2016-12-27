"""
This is version 2
Things to achieve:
Change num_max_repick to be the max value of a random choose.

For instance: if set it to 2,
- it would choose [0-2] from the ones chosen in last week but not
2 weeks in a row,
- and choose [0-3] from the ones chosen in the week before last week.
- if the total number is less than 5, choose from the list of the one have not
been chosen for 2 weeks.
- if the total number still less than 5, add new ones to the list
"""

from itertools import zip_longest
import random

food_count_all = [
    'Asahi',
    'Indian',
    'Sue Ellen',
    'Pizzaria',
    'KingTan',
    'Holiday',
    'Kebab',
    'Meze',
    'Tabuli',
    'Korean',
    'Jappi',
    'Japanese',
    'Amazing Thai',
    'Pong']
food_count_chosen = set()

num_max_repick = 2
num_week_total = 10

booking = {}

for w in range(1, num_week_total+1):
    print('---- WEEK %s ----' % w)
    choice_of_week_current = []
    choice_of_week_last = set(booking.get(w-1, []))
    choice_of_week_before_last = set(booking.get(w-2, []))

    # Choose Max num_max_repick from last week
    tmp_1 = list(choice_of_week_last-choice_of_week_before_last)
    pick_last_week = tmp_1[:random.randrange(num_max_repick)]

    # Choose Max 5-num_max_repick from the week before last week
    tmp_2 = list(choice_of_week_before_last-choice_of_week_last)
    pick_week_before_last_week = tmp_2[:random.randrange(5-num_max_repick)]
    print(
        'The week before last week \t %s' % list(choice_of_week_before_last)
    )
    print(
        'Last week: \t\t\t %s' % list(choice_of_week_last)
    )
    print(
        'We choose them from the week before last week \t %s'
        % (pick_week_before_last_week)
    )
    print(
        'We choose them from last week: \t\t\t %s' % (pick_last_week)
    )
    choice_of_week_current = pick_last_week + pick_week_before_last_week

    # Choose more of the ones have not been chosen for 2 weeks
    num_left = 5 - len(choice_of_week_current)
    if num_left > 0:
        remains = food_count_chosen - choice_of_week_last
        remains = remains - choice_of_week_before_last
        choose_more = list(remains)[:num_left]
        print(
            'We choose more places \t\t\t\t %s' % (choose_more)
        )
        choice_of_week_current = choice_of_week_current + choose_more

    # Choose new places if still not 5 yet
    num_left = 5 - len(choice_of_week_current)
    if num_left > 0:
        max_num = len(food_count_chosen) + 1
        choose_new = list(range(max_num, max_num+num_left))
        print(
            'We choose new places \t\t\t\t %s' % (choose_new)
        )
        choice_of_week_current = choice_of_week_current + choose_new
    booking[w] = choice_of_week_current
    food_count_chosen = food_count_chosen.union(choice_of_week_current)

random.shuffle(food_count_all)
food_count_mapping = dict(zip_longest(food_count_chosen, food_count_all))
print(food_count_mapping)

with open('bookings.log', 'w') as file_:
    for w, ids in booking.items():
        new_list = list({k: food_count_mapping[k] for k in ids}.items())
        random.shuffle(new_list)
        format_mon = ' - Monday: \t%s (%s)\n' % (new_list[0][1], new_list[0][0])
        format_tue = ' - Tuesday: \t%s (%s)\n' % (new_list[1][1], new_list[1][0])
        format_wed = ' - Wednesday: \t%s (%s)\n' % (new_list[2][1], new_list[2][0])
        format_thu = ' - Thursday: \t%s (%s)\n' % (new_list[3][1], new_list[3][0])
        format_fri = ' - Friday: \t%s (%s)\n' % (new_list[4][1], new_list[4][0])
        format_wk = format_mon + format_tue + format_wed + format_thu + format_fri
        print('Week %s:\n%s' % (w, format_wk))
        file_.write('Week %s:\n%s' % (w, format_wk))
