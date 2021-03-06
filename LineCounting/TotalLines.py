import os;
# How to use this program:
# First create a folder, it can be any name, lets call it "LineCounting".
# Move this python program to "LineCounting".
# Then create a subfolder in "LineCounting" called "Repositories", you can not change this name.
# Then change comment 0 below as it instructs.
# Run the program and it should create "TotalLines.txt".
# Open this to see your line counts.
# You can also check "Repositories" to see the raw data.

def main():
    path = "/Users/Najmoon/GitHub";
    # 0: Absolute path to your folder with all your cloned repositories.
    # For example: All my cloned repositories are in /Users/Najmoon/GitHub/(repositories are here).
    # So I will make path = "/Users/Najmoon/GitHub";
    repositories = os.listdir(path);
    cwd = os.getcwd();

    dict = solve(repositories,path,cwd);
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

def solve(repositories,path,cwd):
    dict = {};

    for repository in repositories:
        if ("DS_Store" in repository): continue;
        os.system("cd " + path + "/" + repository + " && git ls-files | xargs wc -l > " + cwd + "/Repositories/" + repository+".txt");
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
