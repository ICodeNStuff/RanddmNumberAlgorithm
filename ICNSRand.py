import time
//only uses time library
class ICNSRandStream:
    time_epoch = int()

    def gen(min_point = 0, max_point = None):        
        time_epoch_no_decimals = int(time.time())
        time_epoch = time.time()
        rand_base = 100 * (time_epoch - float(time_epoch_no_decimals))
        for i in range(int(str(time_epoch_no_decimals)[-1])):
            rand_base = rand_base * 10
        randnum = int(round(rand_base))
        
        if randnum < min_point:
            print('less')
            while randnum < min_point:
                randnum *= 10
        if max_point != None:
            if randnum > max_point:
                print('higher')
                while randnum > max_point:
                    randnum /=10
                #randnum = randnum * 10
        lastnum = int(round(randnum))
            
            
        return lastnum
        
        
Stream = ICNSRandStream
print(Stream.gen(1, 10))
