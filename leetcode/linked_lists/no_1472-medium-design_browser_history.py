#!/usr/bin/python3

# 1472. Design Browser History
# [Medium]
# 
# You have a browser of one tab where you start on the homepage and you can
# visit another url, get back in the history number of steps or move forward in
# the history number of steps.
# 
# Implement the BrowserHistory class:
# 
#     BrowserHistory(string homepage)   Initializes the object with the homepage
#                                       of the browser.
# 
#     void visit(string url)            Visits url from the current page. It
#                                       clears up all the forward history.
# 
#     string back(int steps)            Move steps back in history. If you can
#                                       only return x steps in the history and
#                                       steps > x, you will return only x steps.
#                                       Return the current url after moving back
#                                       in history at most steps.
# 
#     string forward(int steps)         Move steps forward in history. If you
#                                       can only move forward x steps in the
#                                       history and steps > x, you will forward
#                                       only x steps. Return the current url
#                                       after forwarding in history at most
#                                       steps.
# 
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

# Got a hint to use 2 stacks, but otherwise this is Own Code.

# Visible at:
# https://leetcode.com/problems/design-browser-history/submissions/887702448/

class BrowserHistory:
    # Easy. Keep two stacks, one backHistory comprising all visited urls
    # (including the one that's an argument to __init__ or visit()), and one
    # forwardHistory comprising all urls shifted into the forward history by
    # back().
    #
    # When visit() is called, clear forwardHistory, set visiting to url and
    # append url to backHistory.
    #
    # When back() is called, so long as len(backHistory) > 1, pop a url off
    # backHistory and push it onto forwardHistory for each decrement of step.
    #
    # When forward() is called, so long as len(forwardHistory) > 0, pop a url
    # off forwardHistory and push it onto backHistory for each decrement of
    # step.
    def __init__(self, homepage: str):
        """
        Initializes the object with the homepage of the browser.
        """
        self.visiting = homepage
        self.backHistory = [homepage]
        self.forwardHistory = list()

    def visit(self, url: str) -> None:
        """
        Visits url from the current page. It clears up all the forward history.
        """
        self.forwardHistory.clear()
        self.visiting = url
        self.backHistory.append(url)

    def back(self, steps: int) -> str:
        """
        Move steps back in history. If you can only return x steps in the
        history and steps > x, you will return only x steps. Return the current
        url after moving back in history at most steps.
        """
        while len(self.backHistory) > 1 and steps > 0:
            self.forwardHistory.append(self.backHistory.pop())
            steps -= 1
        return self.backHistory[-1]

    def forward(self, steps: int) -> str:
        """
        Move steps forward in history. If you can only forward x steps in the
        history and steps > x, you will forward only x steps. Return the current
        url after forwarding in history at most steps.
        """
        while len(self.forwardHistory) > 0 and steps > 0:
            self.backHistory.append(self.forwardHistory.pop())
            steps -= 1
        return self.backHistory[-1]


commands = ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]

args = [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]

retVals = [None,None,None,None,"facebook.com","google.com","facebook.com",None,"linkedin.com","google.com","leetcode.com"]

for command, arg, expectedRetVal in zip(commands, args, retVals):
    if command == "BrowserHistory":
        print("instantiated object")
        browserHistory = BrowserHistory(*arg)
        retVal = None
    elif command == "visit":
        print(f"visiting '{arg[0]}' should return None")
        retVal = browserHistory.visit(*arg)
    elif command == "back":
        print(f"hitting back {arg[0]} times should return {expectedRetVal}")
        retVal = browserHistory.back(*arg)
    elif command == "forward":
        print(f"hitting forward {arg[0]} times should return {expectedRetVal}")
        retVal = browserHistory.forward(*arg)
    assert retVal == expectedRetVal, retVal

