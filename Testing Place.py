def initialize():
    '''Initializes the global variables needed for the simulation.
    '''
    global cur_hedons, cur_health
    global cur_time
    global last_activity, last_activity_duration
    global last_finished
    global bored_with_stars, stars
    global rest_dur, rest_time
    global run_dur, run_time
    global textbook_dur, textbook_time

    cur_hedons = 0
    cur_health = 0

    cur_star = None
    cur_star_activity = None
    star_time = 0

    bored_with_stars = False

    last_activity = None
    last_activity_duration = 0

    cur_time = 0
    rest_time = 0
    textbook_time = 0
    run_time = 0
    run_dur = 0
    textbook_dur = 0
    rest_dur = 0
    last_finished = -1000

def get_cur_hedrons():
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
    cur_star_activity = activity
    star_time = cur_time


def perform_activity(activity, duration):
    '''Perform the activity activity for the duration of duration minutes.
    '''
    global cur_time, cur_hedons, cur_health
    global last_activity
    global run_time, textbook_time, rest_time
    global run_dur, textbook_dur, rest_dur
    cur_time += duration
    # remember to account for star
    # remember to account for star
    # remember to account for star
    if activity == "running":
        if run_dur <= 180 and (((cur_time - run_time) >= 120) and ((cur_time - textbook_time >= 120))):
            cur_health += 3 * duration
            if duration <= 10:
                cur_hedons += 2 * duration
            elif duration > 10:
                cur_hedons += 20
                cur_hedons += -2 * (duration - 10)
        elif run_dur <= 180 and (((cur_time - run_time) < 120) or ((cur_time - textbook_time < 120))):
            cur_health += 3 * duration
            cur_hedons += -2 * duration
        elif run_dur > 180 and (((cur_time - run_time) >= 120) and ((cur_time - textbook_time >= 120))):
            cur_health += 3 * 180
            cur_health += duration - 180
            if durations <= 10:
                cur_hedons += 2 * duration
            elif durations > 10:
                cur_hedons += 20
                cur_hedons += -2 * (duration - 10)
        elif run_dur > 180 and (((cur_time - run_time) < 120) or ((cur_time - textbook_time < 120))):
            cur_health += 3 * 180
            cur_health += duration - 180
            cur_hedons += -2 * duration
        run_dur += duration
        run_time = cur_time
        last_activity = "running"

    elif activity == "textbooks":
        cur_health += 2 * duration
        if (((cur_time - run_time) < 120) or ((cur_time - textbook_time < 120))):
            cur_hedons += -2 * duration
        elif (((cur_time - run_time) >= 120) and ((cur_time - textbook_time >= 120))):
            if duration <= 10:
                cur_hedons += duration
            elif durations > 10:
                cur_hedons += 10 - (duration -10)
        textbook_dur += duration
        run_dur = 0
        textbook_time = cur_time
        last_activity = "textbooks"

    elif activity == "resting":
        cur_hedons += 0
        cur_health += 0
        run_time = 0
        textbook_time = 0
        rest_time += duration
        last_activity == "resting"
    else:
        return None

def stars_can_be_taken(activity):
    '''Return True if a star can be used to gain more points for the activity
    activity. Return False otherwise.
    '''
    if (bored_with_stars is False) and (cur_star_activity is activity) and (cur_time - star_time == 0):
        return True
    else:
        return False

def most_fun_activity_minute():
    '''Return the activity which would award the most hedons if performed for
    one minute at the current time.
    '''
    pass

################################################################################
#These functions are not required, but we recommend that you use them anyway
#as helper functions

def get_effective_minutes_left_hedons(activity):
    '''Return the number of minutes during which the user will get the full
    amount of hedons for activity activity'''
    pass

def get_effective_minutes_left_health(activity):
    pass

def estimate_hedons_delta(activity, duration):
    '''Return the amount of hedons the user would get for performing activity
    activity for duration minutes'''
    if activity == "running":
        pass
    elif activity == "textbooks":
        pass
    elif activity == "resting":
        return 0
    else:
        return None


def estimate_health_delta(activity, duration):
    pass

################################################################################

if __name__ == "__main__":
    initialize()
    print(get_cur_health())
    print(get_cur_hedrons())
    perform_activity("running", 120)
    # hp: 3 * 120 = 360
    # hed: 2 * 10 + -2 * 110 = -200
    print(get_cur_health()) # 360
    print(get_cur_hedrons()) # -200
    print(cur_time) # 120
    print(run_time) # 120
    perform_activity("running", 70)
    # hed: -2 * 70 + -200 = -340
    # hp: 360 + 3 * 60 + 10 * 1= 550
    print(get_cur_health())
    print(get_cur_hedrons())
    print(cur_time) # 180
    print(run_time) # 120
    print(textbook_time) # 180
    print(run_dur) # 120
    print(textbook_dur) # 60

#     perform_activity("running", 30)
#     print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
#     print(get_cur_health())            # 90 = 30 * 3                          # Test 2
#     print(most_fun_activity_minute())  # resting                              # Test 3
#     perform_activity("resting", 30)
#     offer_star("running")
#     print(most_fun_activity_minute())  # running                              # Test 4
#     perform_activity("textbooks", 30)
#     print(get_cur_health())            # 150 = 90 + 30*2                      # Test 5
#     print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
#     offer_star("running")
#     perform_activity("running", 20)
#     print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
#     print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
#     perform_activity("running", 170)
#     print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
#     print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10