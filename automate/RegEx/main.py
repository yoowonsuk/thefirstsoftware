text = 'Hi there you here exa_mple@example.com @blabla.com some more text here and there another@example.de another@exampl.ne'

import re

pattern = re.compile("[^ ]+@[^ ]+\.(?:com|de)+")
matches = pattern.findall(text)
matches

\. and .
[naother]
[^ ] non space character
+ at least 1
? 0 or 1
* 0 or more times
{3} three char
{3, 6} three to six
^ beginning of a line or string
$ end of a line or string
[^...] a single character or a range that is not contained within the brackets
?:...|... Or operator For example (?:com|de)

