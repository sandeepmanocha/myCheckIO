def check_connection(network, first, second):
    print(network)
    print("Are friends", first, second)
    frnds_dir = {}
    First_hit = False
    ret = False
    for rel in network:
        f1, f2 = rel.split("-")
        # print(f1,f2)
        if f1 in frnds_dir:
            frnds_dir[f1].append(f2)
        else:
            frnds_dir[f1] = [f2]

    frnds_dir = explode_dir(frnds_dir)

    track_search_out = []
    first_hit_out = []
    print (frnds_dir)
    ret = search_connection(frnds_dir, first, second,
                            track_search_out, first_hit_out)
    # print(track_search_out)
    return ret


def explode_dir(frnds_dir):
    full_expanded_dir = frnds_dir.copy()
    # print("explode")
    # print(full_expanded_dir)

    for friend in frnds_dir:
        for fof in frnds_dir[friend]:
            #print("Current --->",friend, " - ", fof)
            #print(fof ,"in full_expanded_dir ",fof in full_expanded_dir)
            if fof in full_expanded_dir:
                #print(friend," in ",full_expanded_dir[fof], friend in full_expanded_dir[fof])
                if not friend in full_expanded_dir[fof]:
                    full_expanded_dir[fof].append(friend)
            else:
                #frnds_dir[fof] = friend
                full_expanded_dir[fof] = [friend]
    # print(full_expanded_dir)
    #print("End Explode")
    return full_expanded_dir


def search_connection(friends_dir, first, second, track_search=[], first_hit=[]):

    print("---->", "Searching..", first, second, track_search)
    ret = None
    #print("First Hit:",first_hit)
    if True in first_hit:
        return True

    if not first in track_search:
        #print("Adding ", first, " to track_search")
        track_search.append(first)
        # print(track_search)
    else:
        # Already Searched for this
        return False

    if first == second:
        print(first, "==", second)
        return False

    #print(first in friends_dir)

    # Serach list of Direct Friends for First
    if first in friends_dir:
        #print(first, "in friends_dir")
       # print("print(second in friends_dir[first])",second in friends_dir[first])
        if second in friends_dir[first]:
            #print("-------------------------->Found One")
            first_hit.append(True)
            # print(first_hit)
            return True
        else:
            print('Friends of ', first, friends_dir[first])
            for friend in friends_dir[first]:
                #print(friend, " is friend of ", first)
                ret = search_connection(
                    friends_dir, friend, second, track_search, first_hit)
                first_hit.append(ret)

    if not True in first_hit and not second in track_search:
        print("------------>search_connection by 2nd", second)
        ret = search_connection(friends_dir, second,
                                first, track_search, first_hit)
        first_hit.append(ret)

    #print("Last Statement with ", first, second, True in first_hit)
    if True in first_hit:
        return True
    else:
        return False


print(check_connection(
    ("scout3-mr99", "scout3-plane2", "plane2-batman", "batman-cat",
     "robin-batman", "robin-cat", "robin-scout4", "out00-scout4", "base-cat", "base-plane2"),
    "robin", "base"))
