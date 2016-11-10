#!/usr/bin/env python
import json

def main():

    with open("input/2012-WI.json") as f:
        info1 = json.load(f)

    with open("input/2016-WI.json") as f:
        info2 = json.load(f)

    polls1 = dict([(x["pollname"],x) for x in info1["polls"]])
    polls2 = dict([(x["pollname"],x) for x in info2["polls"]])

    # interate over all polls in both years
    for pollName in filter(lambda x: x in polls1.keys(), polls2.keys()):
        print pollName
        poll1 = polls1[pollName] 
        poll2 = polls2[pollName] 

        print poll1["candidates"]
        for ans in poll1["answers"]:
            ans1 = ans["answer"]
            print ans1, ans["candidateanswers"]


if __name__ == "__main__":
    main()
