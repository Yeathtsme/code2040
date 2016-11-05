# code2040


Step III: Needle in a haystack

Next, let’s check your skills for working with collections.

We’re going to send you a dictionary with two values and keys. The first value, needle, is a string. The second value, haystack, is an array of strings. You’re going to tell the API where the needle is in the array.

Grab that dictionary from here, again by POSTing your token:

http://challenge.code2040.org/api/haystack

Locate the needle in the haystack array. You’re going to send back the position, or “index,” of the needle string. The API expects indexes to start counting at 0.

POST your results to:

http://challenge.code2040.org/api/haystack/validate

Use the key token for your token.

Use the key needle for the integer representing where the needle was in the array.

As with the previous step, these endpoints expect you to send JSON dictionaries in the body of the request.

Hint: You’ll probably use a loop to solve this one.

Step IV: Prefix

Great job -- but we’re not done with collections.

In this challenge, the API is going to give you another dictionary. The first value, prefix, is a string. The second value, array, is an array of strings. Your job is to return an array containing only the strings that do not start with that prefix.

Note: The strings in your array should be in the same order as in the original array.

POST your token here:

http://challenge.code2040.org/api/prefix

Once you’ve built your array, POST a dictionary here:

http://challenge.code2040.org/api/prefix/validate

Use the key token for your token.

Use the key array for your array.

As with the previous step, these endpoints expect you to send JSON dictionaries in the body of the request.

Hint: You’ll need a little string-fu to complete this challenge. But rest assured: comparing the beginnings of strings is a common task. Your platform’s standard libraries might even have some code to help you do this.


Step V: The dating game

Great job so far. The last challenge is a little different. You’re going to work with dates and times.

The API will again give you a dictionary. The value for datestamp is a string, formatted as an ISO 8601 datestamp. The value for interval is a number of seconds.

You’re going to add the interval to the date, then return the resulting date to the API. POST your token here:

http://challenge.code2040.org/api/dating

Then POST a dictionary with your results here:

http://challenge.code2040.org/api/dating/validate

Use the key token for your token.

Use the key datestamp for an ISO 8601 datestamp string.

As with the previous step, these endpoints expect you to send JSON dictionaries in the body of the request.

Hints:

Make sure your datestamp is formatted the same way as the one the API gives you.
Dates are hard! Don’t feel badly if you’re scratching your head on this one. Most platforms have libraries to help with date and time tasks. Don’t be afraid of using one to solve this challenge.
