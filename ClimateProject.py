#Cameron Simms
#Started Working on This 10/21/21
Footprint = 0
class ClimateQuery:
    def __init__(self, question, answer, carbonvalue):
        self.question = question
        self.answer = answer
        self.carbonvalue = carbonvalue
    def mquery(self):
            global Footprint
            loopnum = 0
            mchoice = ['1', '2', '3', '4', '5']
            print('Do you ' + self.question)
            for item in self.answer:
                print(mchoice[0 + loopnum] + ': ' + self.answer[0 + loopnum])
                loopnum = loopnum + 1
            useranswer = input("Choose The Number That Applies to You: ")
            Footprint += self.carbonvalue[int(useranswer) - 1]
            print(' ')
            pass

# qtemplate: q = ClimateQuery('', [''], [])
q_1 = ClimateQuery('commute by', ['walking', 'biking', 'driving', 'public transit', 'carpooling'], [0, 0, 1115, 131, 459])
q_2 = ClimateQuery('eat mostly', ['fast food', 'home cooked meals'], [4818, 629])
q_3 = ClimateQuery('eat mostly', ['vegetables/fruit', 'meat', 'breads'], [153, 644, 364])
q_4 = ClimateQuery('turn off the lights when you leave a room?', ['yes', 'no'], [133, 268])
q_5 = ClimateQuery('unplug appliances and chargers when they are not in use?', ['yes', 'no'], [9, 18])
q_6 = ClimateQuery('dry clothes by', ['hanging to dry', 'a dryer', 'both'], [0, 750, 375])
q_7 = ClimateQuery('turn off the water when brushing your teeth?', ['yes', 'no'], [34, 274])
q_8 = ClimateQuery('turn off the tv while watching it?', ['yes', 'no'], [47, 140])
q_9 = ClimateQuery('turn off computers while not in use?', ['yes', 'no'], [29, 90])
q_10 = ClimateQuery('you recycle to the best of your ability?', ['yes', 'no'], [-150, 20])
qList = [q_1, q_2, q_3, q_4, q_5, q_6, q_7, q_8, q_9, q_10]
loop = 0
for element in qList:
    qList[loop].mquery()
    loop = loop + 1
print('Your Carbon Footprint is ' + str(Footprint + 13000) + ' pounds of CO2 a year')
