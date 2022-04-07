# Public Repository for Stats/BioDS OpenDP lecture: Practical Privacy-preservation with Differential Privacy and OpenDP
Slides and notebooks for Stats/BioDS 352: https://stats352.stanford.edu/


Data scientists and statisticians, including industry analysts, scientific researchers and data-driven policy makers, often want to analyze data that contains sensitive personal information that must remain private. However, common techniques for data sharing that attempt to preserve privacy either bring great privacy risks or great loss of information. Moreover, the increasing ability of big data, ubiquitous sensors, and social media to record lives in detail brings new ethical responsibilities to safeguard privacy.

Differential privacy, deriving from roots in cryptography, is a formal, mathematical conception of privacy preservation. It guarantees that any released statistical result does not reveal information about any single individual. That is, the distribution of answers one would get with differentially private algorithms from a dataset that does not include myself must be indistinguishable from the distribution of answers where I have added my own information.

Using differential privacy enables us to provide wide access to statistical information from a privacy sensitive dataset without worries of individual-level information being leaked inadvertently or due to an adversarial attack. In these two classes, we’ll work through some of the fundamental building blocks of differentially private algorithms and the key properties they inherit, as well as overview a programming framework library, OpenDP (https://opendp.org) for building practical DP algorithms.

## Reading

Chapters 4-7 (they’re very short) of Near and Abuah [Programming Differential Privacy](https://programming-dp.com)

## Other materials of possible interest:

[Non-technical Primer](http://hona.kr/papers/files/Primer.pdf)

More on OpenDP: https://opendp.org

Further notebooks, readings and materials available from this current class website: https://opendp.github.io/cs208/ 

[Bibliography](http://people.seas.harvard.edu/~salil/cs208/spring19/cs208_annotated_bibliography.pdf) of connections of DP to statistical and ML topics 
