import os;
# How to use this program:
# First create a folder, it can be any name, lets call it "LineCounting".
# Move this python program to "LineCounting".
# Then create a subfolder in "LineCounting" called "Repositories", you can not change this name.
# Then change comments 0-3 below as they instruct.
# Optionally you can do comments 4-6 if you want.
# Run the program and it should create "CodeLines.txt".
# Open this to see your line counts.
# You can also check "Repositories" to see the raw data.

def main():
    repositories = ["AdventOfCode","Algebra2","APCS","AtCoder","BWSI","CodeForces","CodeJam","CodingBat","CSES","IntroCS","Kattis","KickStart","LIT","MBIT","NoctemVirtual","Personal","Test","Usaco","UsacoTrain"];
    # 0: This is a list of repository names that you want to count. Change this list to include
    # the repositories you want to check for. Make sure these repositories are all in the same folder.
    # For example: ~/Github/(All your reppositories are here) -> Add all the names from this folder to the list.

    extensions = [".cpp",".css",".html",".java",".js",".nlogo",".py",".rkt",".rs"];
    # 1: This is a list of file extensions that you want to check for. Change this list to include the
    # file endings of coding languages you want to check for.
    # For example: I want to count c++, python, and java lines so I will add ".cpp", ".py", and ".java" to the list.

    dict = solve(repositories,extensions);
    fout = open("CodeLines.txt","w");

    st = [];
    mx1,mx2 = 0,0;
    for d in dict:
        st.append(d);
        mx1 = max(len(d),mx1)
        mx2 = max(len(str(dict[d])),mx2)
    st.sort();

    for d in st:
        out = "";
        out += d+":" + (mx1+1-len(d))*" ";
        out += " "*(mx2+1-len(str(dict[d]))) + str(dict[d]);
        out += " lines\n"
        fout.write(out);

def solve(repositories,extensions):
    dict = {};

    for repository in repositories:
        a = "~/GitHub"
        # 2: Absolute path to your folder with all your cloned repositories.
        # For example: All my cloned repositories are in ~/GitHub/(repositories are here).
        # So I will make a = "~/GitHub";

        b = "~/CodingFolder/LineCounting"
        # 3: Absolute path to the folder this python file is in, example is shown.
        # For example: This python file is in ~/CodingFolder/LineCounting/(file is in here).
        # So I will make b = "~/CodingFolder/LineCounting".

        os.system("cd " + a + "/" + repository + " && git ls-files | xargs wc -l > " + b + "/Repositories/" + repository+".txt");
        fin = open("Repositories/"+repository+".txt","r");

        lines = fin.read().split("\n")[:-2];
        lines = [line.strip() for line in lines];
        lines = [[int(line.split()[0]),line.split()[1]] for line in lines];

        for line in lines:
            if (line[0] > 10000): continue;
            # 4: Optional, this doesn't count any files above 10000 lines becuase
            # most of your files arent above 10000 lines and you probably don't want to add
            # files that you didn't make to your line count as you dont want to skew results.
            # You can remove this if you want.

            if ("Std" in line[1]): continue;
            # 5: Optional, only include if you have some files like StdDraw.java
            # that aren't yours and you don't want to count those files.
            # You can remove this if you want.

            # 6: You can add more limitations by doing the following: line[0] = line count, line[1] = file path
            # You can write an if statement comparing something to the line count or looking for a substring
            # in the file path and then writing continue after the if statement to disregard those files to
            # the count.

            str = finddot(line[1])
            if (str in extensions):
                if (str in dict):
                    dict[str] += line[0];
                else:
                    dict[str] = line[0];

    return dict;

def finddot(path):
    li = -1
    for i,c in enumerate(path):
        if (c == "."): li = i;
    if (li == -1):
        return "."
    return path[li:];

main();
