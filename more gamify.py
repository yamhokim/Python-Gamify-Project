def initialize():
    '''Initializes the global variables needed for the simulation.
    '''
    global cur_hedons, cur_health
    global cur_time
    global last_activity, last_activity_duration
    global last_finished
    global bored_with_stars, cur_star, cur_star_activity, star_time
    global rest_dur, rest_time
    global run_dur, run_time
    global textbook_dur, textbook_time

    cur_hedons = 0
    cur_health = 0

    cur_star = 0
    cur_star_activity = None
    star_time = 0

    bored_with_stars = False

    cur_time = 0
    rest_time = 0
    textbook_time = 0
    run_time = 0
    run_dur = 0
    textbook_dur = 0
    rest_dur = 0
    last_finished = -1000

def get_cur_hedons():
    '''Return the amount of herdons the user has.'''
    global cur_hedons
    return cur_hedons

def get_cur_health():
    '''Return the number of health points the user has.'''
    global cur_health
    return cur_health

def offer_star(activity):
    '''Offer a star to be used for the activity activity.'''
    global cur_star, cur_star_activity, star_time
    cur_star += 1
    if cur_star >= 3 and cur_time <= 120:
        bored_with_stars = True
    cur_star_activity = activity
    star_time = cur_time

def perform_activity(activity, duration):
    '''Perform the activity activity for the duration of duration minutes.
    '''
    global cur_time, cur_hedons, cur_health
    global last_activity
    global run_time, textbook_time, rest_time
    global run_dur, textbook_dur, rest_dur
    temp_duration = duration
    if stars_can_be_taken(activity) == True:
        if duration > 10:
            cur_hedons += 30
        elif duration <= 10:
            cur_hedons += 3 * duration
        stars_can_be_taken(activity) == False

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
        last_activity = "running"

    elif activity == "textbooks":
        cur_health += 2 * duration
        if (((cur_time - run_time) < 120) or ((cur_time - textbook_time < 120))) and ((run_time != 0) or (textbook_time != 0) or (cur_time != 0)):
            cur_hedons += -2 * duration
        elif (((cur_time - run_time) >= 120) and ((cur_time - textbook_time >= 120))):
            if duration <= 10:
                cur_hedons += duration
            elif durations > 10:
                cur_hedons += 10 - (duration -10)
        textbook_dur += duration
        run_dur = 0
        cur_time += duration
        textbook_time = cur_time
        last_activity = "textbooks"

    elif activity == "resting":
        cur_hedons += 0
        cur_health += 0
        run_time = 0
        textbook_time = 0
        cur_time += duration
        rest_time += duration
        last_activity == "resting"

    else:
        return None

def stars_can_be_taken(activity):
    '''Return True if a star can be used to gain more points for the activity
    activity. Return False otherwise.
    '''
    global bored_with_stars, cur_star_activity, cur_time, star_time
    if (bored_with_stars is False) and (cur_star_activity is activity) and (cur_time - star_time == 0):
        return True
    else:
        return False

def most_fun_activity_minute():
    '''Return the activity which would award the most hedons if performed for
    one minute at the current time.
    '''
    pass

if __name__ == "__main__":
    initialize()
#     print(cur_health) # 0
#     print(cur_hedons) # 0
#     offer_star("running")
#     perform_activity("running", 5)
#     print(cur_hedons) # 3 * 5 + 2 * 5 = 25
#     print(cur_health) # 3 * 5 = 15
#     perform_activity("resting", 120)
#     perform_activity("running", 6)
#     print(cur_health) # 15 + 6 * 3 = 33
#     print(cur_hedons) # 25 + 2 * 6 = 37

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
    perform_activity("resting", 30)
    offer_star("running")
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
