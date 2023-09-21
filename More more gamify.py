def initialize():
    '''Initializes all the global variables needed for the simulation.
    '''
    global cur_hedons, cur_health
    global cur_time
    global last_activity, last_activity_duration
    global last_finished
    global bored_with_stars, cur_star, cur_star_activity, star_time, star_list
    global rest_dur, rest_time
    global run_dur, run_time
    global textbook_dur, textbook_time

    cur_hedons = 0
    cur_health = 0

    cur_star = 0
    cur_star_activity = None
    star_time = 0

    bored_with_stars = False
    star_list = []

    cur_time = 0
    rest_time = 0
    textbook_time = 0
    run_time = 0
    run_dur = 0
    textbook_dur = 0
    rest_dur = 0


def get_cur_hedons():
    '''Return the amount of herdons the user has at cur_time time.'''
    global cur_hedons
    return cur_hedons

def get_cur_health():
    '''Return the number of health points the user has at cur_time time.'''
    global cur_health
    return cur_health

def offer_star(activity):
    '''Offer a star to be used for the activity activity.'''
    global cur_star, cur_star_activity, star_time
    global star_list, bored_with_stars
    cur_star_activity = activity
    star_time = cur_time
    star_list.append(star_time)
    if len(star_list) < 3:
        bored_with_stars = False
    else:
        for i in range(len(star_list)):
            if star_list[i] - star_list[i-2] < 120:
                bored_with_stars = True
            else:
                bored_with_stars = False



def perform_activity(activity, duration):
    '''Perform the activity activity for the duration of duration minutes.
    '''
    global cur_time, cur_hedons, cur_health
    global last_activity
    global run_time, textbook_time, rest_time
    global run_dur, textbook_dur, rest_dur
    temp_duration = duration
    if star_can_be_taken(activity) == True:
        if duration > 10:
            cur_hedons += 30
        elif duration <= 10:
            cur_hedons += 3 * duration
        star_can_be_taken(activity) == False

    if activity == "running":
        if run_dur < 180:
            while temp_duration > 0 and run_dur < 180:
                cur_health += 3
                temp_duration -= 1
                run_dur += 1
        cur_health += temp_duration
        run_dur += temp_duration
        if ((cur_time - run_time) >= 120) or ((cur_time - textbook_time >= 120)) or (cur_time == 0):
            if duration <= 10:
                cur_hedons += 2 * duration
            elif duration > 10:
                cur_hedons += 20
                cur_hedons += -2 * (duration - 10)
        elif ((cur_time - run_time) < 120) or ((cur_time - textbook_time < 120)):
            cur_hedons += -2 * duration

        cur_time += duration
        run_time = cur_time

    elif activity == "textbooks":
        cur_health += 2 * duration
        if (((cur_time - run_time) < 120) or ((cur_time - textbook_time < 120))) and ((run_time != 0) or (textbook_time != 0) or (cur_time != 0)):
            cur_hedons += -2 * duration
        elif (((cur_time - run_time) >= 120) and ((cur_time - textbook_time >= 120))):
            if duration <= 10:
                cur_hedons += duration
            elif duration > 10:
                cur_hedons += 10 - (duration -10)
        textbook_dur += duration
        run_dur = 0
        cur_time += duration
        textbook_time = cur_time

    elif activity == "resting":
        cur_hedons += 0
        cur_health += 0
        run_time = 0
        textbook_time = 0
        cur_time += duration
        rest_time += duration

    else:
        return None

def star_can_be_taken(activity):
    '''Return True if a star can be used to gain more points for the activity
    activity. Return False otherwise.
    '''
    global bored_with_stars, cur_star_activity, cur_time, star_time
    if (bored_with_stars is False) and (cur_star_activity is activity) and (cur_time - star_time == 0):
        return True
    else:
        return False


def perform_activity_hedon(activity):
    '''Return the number of hedons activity activity will give the user for 1 min at time cur_time.
    '''
    global run_time, textbook_time, rest_time
    global run_dur, textbook_dur, rest_dur

    sum = 0
    if star_can_be_taken(activity) == True:
        sum += 3

    if activity == "running":
        if ((cur_time - run_time) >= 120) or ((cur_time - textbook_time >= 120)) or (cur_time == 0):
            sum += 2
        elif ((cur_time - run_time) < 120) or ((cur_time - textbook_time < 120)):
            sum += -2

    elif activity == "textbooks":
        if (((cur_time - run_time) < 120) or ((cur_time - textbook_time < 120))) and ((run_time != 0) or (textbook_time != 0) or (cur_time != 0)):
            sum += -2
        elif (((cur_time - run_time) >= 120) and ((cur_time - textbook_time >= 120))):
            sum += 1

    else:
        return None

    return sum

def most_fun_activity_minute():
    '''Return the activity which would award the most hedons if performed for
    one minute at the current time.
    '''
    list = []
    resting = 0
    running = perform_activity_hedon("running")
    textbook = perform_activity_hedon("textbooks")
    if resting > running and resting > textbook:
        return "resting"
    elif running > resting and running > textbook:
        return "running"
    else:
        return "textbook"

if __name__ == "__main__":
    initialize()

#     perform_activity("running", 1)
#     perform_activity("running", 1)
#     perform_activity("running", 1)
#     print(cur_hedons)
#     print(cur_health)

#     print(cur_health) # 0
#     print(cur_hedons) # 0
#     perform_activity("running", 5)
#     print(cur_hedons) # 2 * 5 = 10
#     print(cur_health) # 3 * 5 = 15
#     offer_star("running")
#     print(stars_can_be_taken("running")) # True
#     perform_activity("running", 6)
#     print(stars_can_be_taken("running")) # False
#     print(cur_health) # 15 + 6 * 3 = 33
#     print(cur_hedons) # 10 + 6 = 16

#     perform_activity("running", 30)
#     print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
#     print(get_cur_health())            # 90 = 30 * 3                          # Test 2
#     perform_activity("resting", 30)
#     perform_activity("textbooks", 30)
#     print(get_cur_health())            # 150 = 90 + 30*2                      # Test 5
#     print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
#     perform_activity("running", 20)
#     print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
#     print(get_cur_hedons())            # -120 = -80 + 10 * (-2) + 10 * (-2)   # Test 8
#     perform_activity("running", 170)
#     print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
#     print(get_cur_hedons())            # -460 = -120 + 170 * (-2)              # Test 10

    perform_activity("running", 30)
    print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_health())            # 90 = 30 * 3                          # Test 2
    print(most_fun_activity_minute())  # resting                              # Test 3
    perform_activity("resting", 30)
    offer_star("running")
    print(most_fun_activity_minute())  # running                              # Test 4
    perform_activity("textbooks", 30)
    print(get_cur_health())            # 150 = 90 + 30*2                      # Test 5
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10
