def checkio(marbles, step,side='root'):
    #print('---Start---'*10)
    print('------>'*int(step),marbles, step)
    ret=0
    idx=0
    bw = set(marbles)
    pearls_list = list(marbles)
    pearls_list_w = pearls_list.copy()
    pearls_list_b = pearls_list.copy()
    opposite_pearl = {'b':'w','w':'b'}

    if step==0:
        return ret

    print('------>' * int(step), 'Before:', pearls_list, step, side)

    w_count = pearls_list.count('w')
    p_white = round(w_count / len(pearls_list), 2)
    print('------>' * int(step), 'w_count:', w_count, 'p_white:', p_white)

    #print('------>' * int(step), 'Prob: ', step, side, str(w_count)+'/'+str(len(pearls_list)))#, str(len(pearls_list)-w_count)+'/'+str(len(pearls_list)))


    # Draw WHITE
    if pearls_list_w.count('w') > 0:

        idx = pearls_list_w.index('w')
        pearls_list_w[idx] = opposite_pearl['w']
        p_w = checkio(''.join(pearls_list_w), int(step) - 1,'w')
    # Draw BLACK
    if pearls_list_b.count('b') > 0:
        idx = pearls_list_b.index('b')
        pearls_list_b[idx] = opposite_pearl['b']
        checkio(''.join(pearls_list_b), int(step) - 1,'b')
        #print('------>' * int(step), 'After b:', pearls_list_b, step)


        #print('After:', pearls_list, ''.join(pearls_list))
        #print(idx)

    #print('----End----' * 10)
    return ret



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio('wbb', 3)) # == 0.48, "1st example"
    """
    print(checkio('wwb', 3)) # == 0.52, "2nd example"
    print(checkio('www', 3)) # == 0.56, "3rd example"
    print(checkio('bbbb', 1)) # == 0, "4th example"
    print(checkio('wwbb', 4)) # == 0.5, "5th example"
    print(checkio('bwbwbwb', 5)) # == 0.48, "6th example"
    """