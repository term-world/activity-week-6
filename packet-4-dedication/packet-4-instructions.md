## INSTRUCTIONS FOR DEDICATION ASSESSMENT PACKET

You may recall the work you did cleaning the data from the intellectual potential assessment
that extrapolated an intelligence upper limit for each resident from the number of books read.

Our bold and fearless mayor, in his inspired plan to ensure that `term-world`
is a haven for the best and brightest,
has shared the next phase in his citizen potential assessment.

You may already be aware, but `term-world` is outfitted with state-of-the-art
monitoring systems that are able to track how *dedicated* a citizen is to `term-world`.
With these systems we have been able to track a variety of metrics for each citizen,
including (but certainly not limited to):
- The number of lines of code written
- The amount of time spent actively working in `term-world`
- The quantity of words in qualitative reflection documentation
- The number of commits made to `term-world` repositories

The plan is simple: we will leverage the data collected from these monitoring systems
in order to establish a citizen ranking system.

`term-world` is a special place, in that the entire city can be changed in the blink of an eye
with just a few lines of particularly savvy code.
Of course, this means that it's *vulnerable*. 

Our mayor has wisely determined that `term-world` needs to be protected. Safeguarded.
He's come up with a plan to restrict access to certain functions of `term-world` based on how
*dedicated* to the `term-world` cause individual residents are.

In an effort to be fair, we will only be using quantitative data
like the four metrics previously mentioned
to assess whether each resident is *dedicated* enough to be allowed varying levels of permission
in terms of changing and enhancing `term-world` with their code.

The data has been collected and stored in `dedication-data.json`.
This is a `json` file, a special type of file that can be read *as a dictionary*, among other things.
You'll notice the file itself is a large dictionary with *smaller dictionaries inside of it*.
You may need some time to review the data, but I'm sure its organization will eventually make sense to you.

Your job is simple: the `citizen-rank-assigner.py` needs to be finished.
When complete, it will take the data on a particular citizen,
and ultimately determine which "rank" that citizen ought to be given.

We've included a separate `citizen-rank-specifications.md` document that
specifies the thresholds citizens must meet across their dedication metrics
to acheive particular ranks. You'll want to refer to that as you work.

As always, our city is counting on you.