# What's this then?

This is my solution for a practice exercise assigned as part of a software development course. It  was assigned on the second day of the fifth week (Tuesday 15th March 2022).

The "startpoint" directory contains the source files provided with the assignment, and "task.md" contains the instructions we were given. The single file "task_list.py" comprises my solution to the task set (in this particular case, it is purely coincidental that the work "task" appears in both "task.md" and the solution's file name, so it might be a bit confusing if one assumes there is a connection when there is none).


# Right... but what does it do?

It's basically an interactive To Do List. The Python code runs in the terminal and the user can control it by typing inputs based on prompts that the code generates as needed.

One slightly odd behaviour arises from my interpretation of the specificity of the instructions, which asked the following of my code:

> 1. Print a list of uncompleted tasks
> 
> 2. Print a list of completed tasks
> 
> 3. Print a list of all task descriptions

To me, that sounds like the first two want the full details of the tasks (in this case that means description, duration, and whether they're completed yet or not), whereas the third specifically and exclusively wants the output to be from the description field without any of the other data. In practice, this seems like an odd way to structure a program, but I've opted to follow the instructions explicitly and precisely even so.

To be honest, I suspect this is probably just a minor oversight in the phrasing of the instructions and the intention was for all three to list the data in the same way, although I can't quite decide whether all three were meant to list only the descriptions or the other data as well. In any case, I listed only the description for the unfiltered list of tasks, and the description and duration for the filtered completed and incomplete task lists (since their completion status is implicit given that the user is explicitly requesting those filtered lists based on whether the tasks are completed or otherwise).

Apart from that, I've mostly avoided straying too far from the instructions because of time limitations. I'm still working in my unrelated day job and we weren't told that we were to submit this as a homework exercise until long after teaching had finished for the day and I had started my shift, so I have had little choice but to stay awake into the early hours of the morning to get this done. The alternative was not doing it at all and potentially learning nothing from it, so I chose to bite the bullet instead.