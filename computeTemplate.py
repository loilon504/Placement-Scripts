import os

score = [0] * 50000
scoreSecond = [0] * 50000
time = [0] * 50000
timeSecond = [0] * 50000
count = [0] * 50000
type = [""] * 3

outputFile = "computePlaMat.txt"        ########################################NeedChange###################################################

def getType():
    global outputFile
    type[1] = outputFile[7:10].lower()
    if len(outputFile) > 14: 
        type[2] = outputFile[10:13].lower()
        if not type[2] in ["spr", "tbr", "mat"]: type[2] = ""

def getInt(line):
    tmpInt = 0
    for t in line:
        if t.isdigit():
            tmpInt = tmpInt * 10 + int(t)
    return tmpInt

def getRealTime(line):
    tmpMinute = tmpSecond = 0
    cntDecimal = 1
    state = 0
    for t in line:
        if t == 'm': state = 1
        if t == ".": state = 2
        if t.isdigit():
            if state == 0: tmpMinute = tmpMinute * 10 + int(t)
            else:
                if state == 2: cntDecimal *= 10
                tmpSecond = tmpSecond * 10 + int(t)
    return tmpMinute * 60 + tmpSecond / cntDecimal

def getFloat(line):
    tmpFloat = 0
    cntDecimal = 1
    ok = False
    for t in line:
        if t == ".": 
            ok = True
            continue
        if t.isdigit():
            if ok == True: cntDecimal *= 10
            tmpFloat = tmpFloat * 10 + int(t)
    return tmpFloat / cntDecimal


def init():
    global score
    global time
    global count
    global scoreSecond
    global timeSecond
    with open(outputFile, 'a') as file: pass
    with open(outputFile, 'r') as file:
        state = 0
        for line in file:
            if line[:6] == "Usher-":
                state = getInt(line)
                continue
            if line[:10] == "Placement-":
                state = getInt(line)
                continue
            if line[:6] == "Score:":
                score[state] += getInt(line)
                continue
            if line[:12] == "ScoreSecond:":
                scoreSecond[state] += getInt(line)
                continue
            if line[:5] == "Time:":
                time[state] += getFloat(line)
                continue
            if line[:11] == "TimeSecond:":
                timeSecond[state] += getFloat(line)
            if line[:6] == "Count:":
                count[state] += getInt(line)

def saveResult():
    global score
    global time
    global count
    global scoreSecond
    global timeSecond
    with open(outputFile, 'w') as file: pass
    # for i in [9909, 19767, 29624, 42448]:
    for i in [200, 500, 1000, 2000, 5000, 10000]:
        with open(outputFile, 'a') as file:
            if type[1] == "ush": file.write("Usher-" + str(i) + "\n")
            if type[1] == "pla": file.write("Placement-" + str(i) + "\n")
            file.write("Score: " + str(score[i]) + "\n")
            file.write("Time: " + str(time[i]) + "\n")
            file.write("Count: " + str(count[i]) + "\n")
            if type[2] != "":
                file.write("ScoreSecond: " + str(scoreSecond[i]) + "\n")
                file.write("TimeSecond: " + str(timeSecond[i]) + "\n")
            if count[i] != 0:
                file.write("Average Score: " + str(score[i] / count[i]) + "\n")
                file.write("Average Time: " + str(time[i] / count[i]) + "\n")
                if type[2] != "":
                    file.write("Average ScoreSecond: " + str(scoreSecond[i]  / count[i]) + "\n")
                    file.write("Average TimeSecond: " + str((time[i] + timeSecond[i]) / count[i]) + "\n")
            file.write("\n")

getType()
init()
print(type)
# for i in [9909, 19767, 29624, 42448]:
for i in [200, 500, 1000, 2000, 5000, 10000]:
# for i in [200, 500]:
    # preFileName = "test" + str(i) + "/matPlaRun"
    preFileName = "testUsher/usherRun"          ########################################NeedChange###################################################
    for j in range(6):
        fileName = preFileName + str(i) + "-" + str(j) + ".txt"
        if not os.path.exists(fileName): 
            continue

        ok = False
        okSecond = False
        with open(fileName, 'r') as file:
            for line in file:
                # compute Placement/UShER score       
                if ok == False:
                    check = False
                    if type[1] == "pla" and line[:8] == "New tree": check = True
                    if type[1] == "ush" and line[:37] == "The parsimony score for this tree is:": check = True
                    if check == True:
                        ok = True
                        score[i] += getInt(line)
                        count[i] += 1
                # compute Second score
                if type[2] != "" and okSecond == False:
                    check = False
                    if type[2] in ["spr", "tbr"] and line[:11] == "Score after": check = True
                    if type[2] == "mat" and line[:22] == "Final Parsimony score:": check = True
                    if check == True:
                        okSecond = True
                        scoreSecond[i] += getInt(line)
                
                # compute Placement/UShER time
                if ok and okSecond == False:
                    if line[:4] == "real": time[i] += getRealTime(line)
                    # if type[1] == "pla" and line[:5] == "Time:": time[i] += getFloat(line)
                    # if type[1] == "ush" and line[:17] == "UShER total time:": time[i] += getFloat(line)

                # compute Second time
                if okSecond and line[:4] == "real": timeSecond[i] += getRealTime(line)

    # print log
    if type[1] == "pla": print("Placement-" + str(i))
    if type[1] == "ush": print("Usher-" + str(i))
    print("Score:", score[i])
    print("Time:", time[i])
    print("Count:", count[i])
    if type[2] != "":
        print("ScoreSecond:", scoreSecond[i])
        print("TimeSecond:", timeSecond[i])
    if count[i] != 0:
        print("Average Score:", score[i] / count[i])
        print("Average Time:", time[i] / count[i])
        if type[2] != "":
            print("Average ScoreSecond:", scoreSecond[i] / count[i])
            print("Average TimeSecond:", (time[i] + timeSecond[i]) / count[i])
    print()
saveResult()
