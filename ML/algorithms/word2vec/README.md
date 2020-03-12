## diff bettween CBOW and Skip-Gram
- CBOW, predict the center word from context
    - Statistically it has the effect that CBOW smoothes over a lot of the distributional information (by treating an entire context as one observation). 
    - For the most part, this turns out to be a useful thing for smaller datasets. 
- Skip-Gram
    - skip-gram treats each context-target pair as a new observation, and this tends to do better when we have larger datasets.
    
    
