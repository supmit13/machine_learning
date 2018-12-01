import os, sys, re, time

if __name__ == "__main__":
    ftest = open("UCI_test.csv", "r")
    all_lines = ftest.readlines()
    ftest.close()

    fdump = open("classified_stability_tmp.txt", "r")
    dump_lines = fdump.readlines()
    fdump.close()

    test_list = []
    dump_list = []
    for testline in all_lines:
        lineparts = testline.split(",")
        status = lineparts[lineparts.__len__() - 1]
        status = status.replace('"', '')
        test_list.append(status)

    for dumpline in dump_lines:
        dumplineparts = dumpline.split(" ")
        status = dumplineparts[dumplineparts.__len__() - 1]
        dump_list.append(status)

    j = 1
    for i in range(all_lines.__len__()):
        if test_list[i] != dump_list[i]:
            print test_list[i], "$$$$$$"
            print dump_list[i], "@@@@@@@"
            print "Failed # %s\n"%j
            j += 1
    print "Count = %s\n"%j
    print "Done!\n"
