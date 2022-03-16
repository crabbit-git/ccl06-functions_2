# What's this then?

This is my solution for a practice exercise assigned as part of a software development course. It  was assigned on the second day of the fifth week (Tuesday 15th March 2022).

The "startpoint" directory contains the source files provided with the assignment, and "task.md" contains the instructions we were given. The single file "task_list.py" comprises my solution to the task set (in this particular case, it is purely coincidental that the work "task" appears in both "task.md" and the solution's file name, so it might be a bit confusing if one assumes there is a connection when there is none).


# Right... but what does it do?

It's basically an interactive To Do List.

One slightly odd behaviour arises from my interpretation of the specificity of the instructions, which asked the following of my code:

> 1. Print a list of uncompleted tasks
> 
> 2. Print a list of completed tasks
> 
> 3. Print a list of all task descriptions

To me, that sounds like the first two want the full details of the tasks (in this case that means description, duration, and whether they're completed yet or not), whereas the third specificaly and exclusively wants the output to be from the description field without any of the other data. In practice, this seems like an odd way to structure a program, but I've opted to follow the instructions explicitly and precisely even so. I suspect this is probably just a minor oversight in the phrasing of the instructions, however, and the intention was for all three to list the data in the same way, although I can't quite decide whether all three were meant to list only the descriptions or the other data as well. In any case, I listed only the description for the unfiltered list of tasks, and the description and duration for the filtered completed and incomplete task lists (since their completion status is implicit given that the user is explicitly requesting those filtered lists based on whether the tasks are completed or otherwise).
