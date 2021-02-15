import os;
# How to use this program:
# First create a folder, it can be any name, lets call it "LineCounting".
# Move this python program to "LineCounting".
# Then create a subfolder in "LineCounting" called "Repositories", you can not change this name.
# Then change comments 0-2 below as they instruct.
# Run the program and it should create "TotalLines.txt".
# Open this to see your line counts.
# You can also check "Repositories" to see the raw data.

def main():
    repositories = ["AdventOfCode","Algebra2","APCS","AtCoder","BWSI","CodeForces","CodeJam","CodingBat","CSES","IntroCS","Kattis","KickStart","LIT","MBIT","NoctemVirtual","Personal","Test","Usaco","UsacoTrain"];
    # 0: This is a list of repository names that you want to count. Change this list to include
    # the repositories you want to check for. Make sure these repositories are all in the same folder.
    # For example: ~/Github/(All your reppositories are here) -> Add all the names from this folder to the list.

    dict = solve(repositories);
    fout = open("TotalLines.txt","w");

    st = []
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

def solve(repositories):
    dict = {};

    for repository in repositories:
        a = "~/GitHub"
        # 1: Absolute path to your folder with all your cloned repositories.
        # For example: All my cloned repositories are in ~/GitHub/(repositories are here).
        # So I will make a = "~/GitHub";

        b = "~/CodingFolder/LineCounting"
        # 2: Absolute path to the folder this python file is in, example is shown.
        # For example: This python file is in ~/CodingFolder/LineCounting/(file is in here).
        # So I will make b = "~/CodingFolder/LineCounting".

        os.system("cd " + a + "/" + repository + " && git ls-files | xargs wc -l > " + b + "/Repositories/" + repository+".txt");
        fin = open("Repositories/"+repository+".txt","r");

        lines = fin.read().split("\n")[:-2];
        lines = [line.strip() for line in lines];
        lines = [[int(line.split()[0]),line.split()[1]] for line in lines];

        for line in lines:
            str = finddot(line[1])
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
