# Name:- Sharvari Kiran Bore
# Student Number:- 201700963

cache = list()
requests = list()
occurance = dict()

while True:
    user_input = input("Press 1 for FIFO, Press 2 for LFU, or Press Q to QUIT the program.: ").capitalize()



    def fifo(request):
        while request != 0:
            if request in cache:
                print('Hit') 
            elif request not in cache and len(cache) < 8:
                cache.append(request)
                # print('cachee111111111', cache)
                print("Miss")
            elif request not in cache and len(cache) > 7:
                cache.pop(0)
                cache.append(request)
                # print('cachee222222', cache)
                print("Miss")
                # break
                # print(cache)
            return cache

    def getKeyFromValue(dict, val):
        dictKeys = [k for k, 
                v in dict.items() 
                if v == val]
        if dictKeys:
            return dictKeys[min(occurance.keys())]
        return None


    def lfu(request):
        while request != 0:
            if request in cache:
                print('Hit')
                occurance[request] += 1
                # print(occurance)
                return
                #requests[request] += 1
            elif request not in cache and len(cache) < 8:
                cache.append(request)
                occurance[request] = 1
                # print(occurance)
                # print('cachee111111111', cache)
                print("Miss")
                return
            elif request not in cache and len(cache) > 7:
                
                minOccuranceValue = min(occurance.values())
                # print('minOccuranceValue',minOccuranceValue)

                minOccuranceValueKey = getKeyFromValue(occurance,minOccuranceValue)
                # print('minOccuranceValueKey',minOccuranceValueKey)

                popIndex = cache.index(minOccuranceValueKey)
                # print('cacheIndex',popIndex)

                cache.pop(popIndex)
                cache.append(request)

                # print('occurance',occurance)

                # cache.pop(minOccuranceValueKey)



            return
        return cache



        # if user_input == "1":


    while True:
        if user_input == "Q":
            exit()
        value = int(input("enter number: "))
        requests.append(value)
        if value != 0: 
            if user_input == "1":
                fifo(value)
            # else:
            #     print("Cache List", cache)
            #     print("Request List", requests)
            #     cache.clear()
            #     break
            elif user_input == "2":
                lfu(value)
        # while True:
        #     value = int(input("enter number: "))
        #     requests.append(value)
                
        else:
            print("Cache list", cache)
            print("Request list", requests)
            cache.clear()
            requests.clear()
        break
    

# cache.append(val)

# def fifo(value):
#   # while True:
#   #   if value not in cache:
#   #     cache.append(value)
#   #     print('cacheeeeeeeee',cache)
#   #     print("Miss - add ",value, " to cache")
#   # else:
#   #     print("Hit - already got ",value," in cache")
#   # return value

#  while True:
#     # print('enter a number'),int(input())
#     # val = int(input())
#     if value not in cache:
#         cache.append(value)
#         print('sssssss',value)
#     # else:
#     #     a.sort()
#     #     for i in a:
#     #         print(i)

#     #     for i in a:
#     #         if i not in notRepeatedList:
#     #             notRepeatedList.append(i)
#     #             print('Repeated', a)
#     #             print('Not Repeated', notRepeatedList)
#         break


# print('dsdsddsd',fifo())


# elif user_input == 2:
#   lfu()
# elif user_input == Q:
#   quit
