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
    global star_list

    star_list = []

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
    global cur_star, cur_star_activity, star_time, star_list, bored_with_stars

    cur_star_activity = activity
    star_time = cur_time
    star_list.append(star_time)
    if len(star_list) < 3:
        bored_with_stars = False
    else:
        if star_list[-1] - star_list[-3] < 120:
            bored_with_stars = True

def perform_activity(activity, duration):
    '''Perform the activity activity for the duration of duration minutes.
    '''
    global cur_time, cur_hedons, cur_health
    global last_activity
    global run_time, textbook_time, rest_time
    global run_dur, textbook_dur, rest_dur
    temp_duration = duration

    if activity == "running":
        if run_dur < 180:
            while temp_duration > 0 and run_dur < 180:
                cur_health += 3
                temp_duration -= 1
                run_dur += 1
        cur_health += temp_duration
        run_dur += temp_duration
        if (((cur_time - run_time) >= 120) and ((cur_time - textbook_time >= 120))) or (cur_time == 0):
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
            if duration <= 20:
                cur_hedons += duration
            elif durations > 20:
                cur_hedons += 20
                cur_hedons -= (duration - 20)
        textbook_dur += duration
        run_dur = 0
        cur_time += duration
        textbook_time = cur_time

    elif activity == "resting":
        cur_hedons += 0
        cur_health += 0
        run_dur = 0
        cur_time += duration
        rest_time += duration

    else:
        return None

    if star_can_be_taken(activity) == True:
        if duration > 10:
            cur_hedons += 30
        elif duration <= 10:
            cur_hedons += 3 * duration

    cur_star_activity = None
def star_can_be_taken(activity):
    '''Return True if a star can be used to gain more points for the activity
    activity. Return False otherwise.
    '''
    global bored_with_stars, cur_star_activity, cur_time, star_time
    if (bored_with_stars == False) and (cur_star_activity == activity) and (cur_time - star_time == 0):
        return True
    else:
        return False


def perform_activity_hedon(activity):
    global run_time, textbook_time, rest_time
    global run_dur, textbook_dur, rest_dur

    sum = 0
    if star_can_be_taken(activity) == True:
        sum += 3

    if activity == "running":
        if (((cur_time - run_time) >= 120) and ((cur_time - textbook_time >= 120))) or (cur_time == 0):
            sum += 2
        elif ((cur_time - run_time) < 120) or ((cur_time - textbook_time < 120)):
            sum += -2

    elif activity == "textbooks":
        if (((cur_time - run_time) < 120) or ((cur_time - textbook_time < 120))) and ((run_time != 0) or (textbook_time != 0) or (cur_time != 0)):
            sum += -1
        elif (((cur_time - run_time) >= 120) and ((cur_time - textbook_time >= 120))):
            sum += 1
    else:
        return None

    return sum

def most_fun_activity_minute():
    '''Return the activity which would award the most hedons if performed for
    one minute at the current time.
    '''
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
    offer_star("textbooks")
    perform_activity("running", 110)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 90)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 130)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    offer_star("running")
    perform_activity("textbooks", 30)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 100)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    print(most_fun_activity_minute())
    perform_activity("textbooks", 120)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 100)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 20)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("running", 50)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 110)
    print(get_cur_health())
    print(get_cur_hedons())
    print(most_fun_activity_minute())
    perform_activity("resting", 10)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("resting", 60)
    print(get_cur_health())
    print(get_cur_hedons())
    offer_star("textbooks")
    perform_activity("running", 70)
    print(get_cur_health())
    print(get_cur_hedons())
    perform_activity("textbooks", 40)
    print(get_cur_health())
    print(get_cur_hedons())

# 330
#  -180
#  560
#  -360
#  820
#  -620
#  resting
#  880
#  -680
#  1080
#  -880
#  resting
#  resting
#  1320
#  -1120
#  1620
#  -1320
#  1620
#  -1320
#  1770
#  -1420
#  1770
#  -1420
#  resting
#  1770
#  -1420
#  1770
#  -1420
#  1980
#  -1520
#  2060
#  -1600