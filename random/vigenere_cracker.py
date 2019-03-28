message = "KNEIWNQBKFEOQXCUMSIYBJKEWNLBZYBFDBVNSAEZBPADGBAAXFHEHUXSFQOFCADPAFAFQGPLZEA"
          #KNEII_PCS_EOQXPGLTQSBJKEI_KCGSBFDBH_RBMTBPADTO_BE_HEHUJEERW_CADPNS_GYAPLZEN
          #KNEKJEPUB_EOQZQLLK_SBJKGJEKUQSBFDDIERTWTBPAFUT_TO_HEHWKJEIF_CADROX_YHAPLZGO
          #KNEKKEPUB_EOQZRLLK_SBJKGKEKUQSBFDDJERTWTBPAFVT_TO_HEHWLJEIF_CADRPX_YHAPLZGP
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key_len = 10
should_lock_char = [False, False, False, False, False, False, False, False, False, False]
lock_num = [0,0,0,0,0,0,0,0,0,0]
lock_trigger = False
lock_words = ["_THE_", "_BE_"]

message_chunks = [message[i:i+key_len] for i in range(0, len(message), key_len)]

def shift_msg(msg_chunks, shift_offset) :
    chunks = [""] * key_len * len(msg_chunks)
    for i in range(key_len):
        j = 0
        for chunk in msg_chunks:
            if(len(chunk) > i):
                chunks[(j * key_len) + i] = alphabet[alphabet.find(chunk[i]) + shift_offset[i]]
                j+=1
    return "".join(chunks)

def print_if_possibility(msg, shift_list):
    if(not ("_THE_" in msg or "_BE_" in msg or "_TO_" in msg)) :
        return
    global lock_trigger
    if(not lock_trigger):
        num = 0
        for str in lock_words:
            if str not in msg:
                print(msg)
                return
        for n in len(lock_words):
            pos = msg.find(lock_words[n]) % 10
            for i in range(pos, pos+len(lock_words[n])):
                should_lock_char[i] = True
                lock_num[i] = shift_list[i]
            lock_trigger = True
    print(msg)

# TODO: Define this in a better way using key_len instead

# for a in range(27):
#     if(lock_char[0]):
#         continue
#     for b in range(27):
#         if(lock_char[1]):
#             continue
#         for c in range(27):
#             if(lock_char[2]):
#                 continue
#             for d in range(27):
#                 if(lock_char[3]):
#                     continue
#                 for e in range(27):
#                     if(lock_char[4]):
#                         continue
#                     for f in range(27):
#                         if(lock_char[5]):
#                             continue
#                         for g in range(27):
#                             if(lock_char[6]):
#                                 continue
#                             for h in range(27):
#                                 if(lock_char[7]):
#                                     continue
#                                 for i in range(27):
#                                     if(lock_char[8]):
#                                         continue
#                                     for j in range(27):
#                                         if(lock_char[9]):
#                                             continue
#                                         print_if_possibility(shift_msg(message_chunks, [j,i,h,g,f,e,d,c,b,a]))

def a() :
    shift_list = [0] * 10
    if(not should_lock_char[0]):
        for i in range(27) :
            shift_list[0] = i
            if(not should_lock_char[0]):
                b(shift_list)
            else:
                break
    if(should_lock_char[0]):
        shift_list[0] = lock_num[0]
        b(shift_list)

def b(shift_list):
    if(not should_lock_char[1]):
        for i in range(27) :
            shift_list[1] = i
            if(not should_lock_char[1]):
                c(shift_list)
            else:
                break
    if(should_lock_char[1]):
        shift_list[1] = lock_num[1]
        c(shift_list)

def c(shift_list):
    if(not should_lock_char[2]):
        for i in range(27) :
            shift_list[2] = i
            if(not should_lock_char[2]):
                d(shift_list)
            else:
                break
    if(should_lock_char[2]):
        shift_list[2] = lock_num[2]
        d(shift_list)

def d(shift_list):
    if(not should_lock_char[3]):
        for i in range(27) :
            shift_list[3] = i
            if(not should_lock_char[3]):
                e(shift_list)
            else:
                break
    if(should_lock_char[3]):
        shift_list[3] = lock_num[3]
        e(shift_list)

def e(shift_list):
    if(not should_lock_char[4]):
        for i in range(27) :
            shift_list[4] = i
            if(not should_lock_char[4]):
                f(shift_list)
            else:
                break
    if(should_lock_char[4]):
        shift_list[4] = lock_num[4]
        f(shift_list)

def f(shift_list):
    if(not should_lock_char[5]):
        for i in range(27) :
            shift_list[5] = i
            if(not should_lock_char[5]):
                g(shift_list)
            else:
                break
    if(should_lock_char[5]):
        shift_list[5] = lock_num[5]
        g(shift_list)

def g(shift_list):
    if(not should_lock_char[6]):
        for i in range(27) :
            shift_list[6] = i
            if(not should_lock_char[6]):
                h(shift_list)
            else:
                break
    if(should_lock_char[6]):
        shift_list[6] = lock_num[6]
        h(shift_list)

def h(shift_list):
    if(not should_lock_char[7]):
        for n in range(27) :
            shift_list[7] = n
            if(not should_lock_char[7]):
                i(shift_list)
            else:
                break
    if(should_lock_char[7]):
        shift_list[7] = lock_num[7]
        i(shift_list)

def i(shift_list):
    if(not should_lock_char[8]):
        for i in range(27) :
            shift_list[8] = i
            if(not should_lock_char[8]):
                j(shift_list)
            else:
                break
    if(should_lock_char[8]):
        shift_list[8] = lock_num[8]
        j(shift_list)

def j(shift_list):
    if(not should_lock_char[9]):
        for i in range(27) :
            shift_list[9] = i
            if(not should_lock_char[9]):
                print_if_possibility(shift_msg(message_chunks, shift_list), shift_list)
            else:
                break
    if(should_lock_char[9]):
        shift_list[9] = lock_num[9]
        print_if_possibility(shift_msg(message_chunks, shift_list), shift_list)

a()
