## Client Services
**`class MojangAPI.Client.User()`**
    <p>
        &ensp;&ensp;&ensp;Represents a minecraft User. This class is used for all User related methods, including changing skin, getting player data and more.  
        &ensp;&ensp;&ensp;This class also inherits the methods of the Auth class.
    </p>
    <p>
        &ensp;&ensp;&ensp;**`minecraftUsername`**
        <p>
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;A players in-game name
        </p>
    </p>
    <p>
        &ensp;&ensp;&ensp;**`mojangUsername`**
        <p>
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;A players mojang account name, this will most likely be their email.
        </p>
    </p>
    <p>
        &ensp;&ensp;&ensp;**`uuid`**
        <p>
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;A players unique id that will be used when performing numerous actions.
        </p>
    </p>
    <p>
        &ensp;&ensp;&ensp;**`authenticated`**
        <p>
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;A boolean representing whether or not a User has authenticated themself.
        </p>
    </p>
    <p>
        &ensp;&ensp;&ensp;**`accessToken`**
        <p>
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;A token that allows a user to connect to their Mojang account, is received upon authenticating.
        </p>
    </p>
    <p>
        &ensp;&ensp;&ensp;**`clientToken`**
        <p>
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;A token generated when a User is created, allows the player to stay authenticated whilst the program is running.
        </p>
    </p>
    <p>
        &ensp;&ensp;&ensp;**`await getUUID(username, time=None)`**
        <p>
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;This function is a *[coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine "a coroutine")*.  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;This gets called by default when creating a new User.
        </p>
    </p>
    <p>
        &ensp;&ensp;&ensp;**`await getNameHistory()`**
        <p>
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;This function is a *[coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine "a coroutine")*.   
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Returns a list of dictionaries containing a players past usernames.
        </p>
    </p>
        <p>
        &ensp;&ensp;&ensp;**`await getProfile()`**
        <p>
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;This function is a *[coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine "a coroutine")*.  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Returns a Profile class containing the following:  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;> ID  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;> Username  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;> Skin URL  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;> Cape URL  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;> Timestamp  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;> Raw response
        </p>
    </p>
    <p>
        &ensp;&ensp;&ensp;**`await changeSkin(skin_url, slimModel = False)`**
        <p>
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;This function is a *[coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine "a coroutine")*.  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Changes a players skin to the skin found in the URL.  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;```Note: This requires the user to have authenticated and for the IP to be trusted```
        </p>
    </p>
    <p>
        &ensp;&ensp;&ensp;**`await uploadSkin(file, slimModel = False)`**
        <p>
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;This function is a *[coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine "a coroutine")*.  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Uploads a skin to Mojang's servers and changes the skin of the user.  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;```Note: This requires the user to have authenticated and for the IP to be trusted```
        </p>
    </p>
    <p>
        &ensp;&ensp;&ensp;**`await resetSkin(file, slimModel = False)`**
        <p>
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;This function is a *[coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine "a coroutine")*.  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Resets the users skin back to the default skin.   
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;```Note: This requires the user to have authenticated and for the IP to be trusted```
        </p>
    </p>
    <p>
        &ensp;&ensp;&ensp;**`await checkForSecurityQuestions()`**
        <p>
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;This function is a *[coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine "a coroutine")*.  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Returns True if the IP is not trusted by Mojang's servers.  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;```Note: This requires the user to have authenticated```
        </p>
    </p>
    <p>
        &ensp;&ensp;&ensp;**`await getSecurityQuestions()`**
        <p>
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;This function is a *[coroutine](https://wiki.vg/Mojang_API#Get_list_of_questions "a coroutine")*.  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Returns a list of security questions in the format seen [here](https://docs.python.org/3/library/asyncio-task.html#coroutine "Mojang API").  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;```Note: This requires the user to have authenticated```
        </p>
    </p>
    <p>
        &ensp;&ensp;&ensp;**`await sendSecurityAnswers(answers)`**
        <p>
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;This function is a *[coroutine](https://wiki.vg/Mojang_API#Get_list_of_questions "a coroutine")*.  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Sends back a list of answers to the given security questions in order for Mojang's servers to trust a Users IP.  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;(i believe this only has to be done once)  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;The list of answers should follow the format seen [here](https://wiki.vg/Mojang_API#Send_back_the_answers "Mojang API").  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;```Note: This requires the user to have authenticated```
        </p>
    </p>
    <p>
        <br/><br/>
        **`class MojangAPI.Client.Auth()`**
        <p>
            &ensp;&ensp;&ensp;Stores authentication methods that will be inherited by the User class.  
        </p>
    </p>
    <p>
        &ensp;&ensp;&ensp;**`await authenticate(username, password)`**
        <p>
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;This function is a *[coroutine](https://wiki.vg/Mojang_API#Get_list_of_questions "a coroutine")*.  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;This authenticates a User given their Mojang username and password.  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Saves the returned accessToken and sets the *authenticated* attribute of the User to True.  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Returns a dictionary containing all the information returned after authenticating.
        </p>
    </p>
    <p>
        &ensp;&ensp;&ensp;**`await refresh()`**
        <p>
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;This function is a *[coroutine](https://wiki.vg/Mojang_API#Get_list_of_questions "a coroutine")*.  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Refreshes a valid access token.  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Sets the *accessToken* attribute of the User to the new token and returns a dictionary containing the response information.  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;```Note: This requires the user to have authenticated```
        </p>
    </p>
    <p>
        &ensp;&ensp;&ensp;**`await validate()`**
        <p>
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;This function is a *[coroutine](https://wiki.vg/Mojang_API#Get_list_of_questions "a coroutine")*.  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Checks if a users access token is usable for authentication with a minecraft server.  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Returns True if the token is valid else False  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;```Note: This requires the user to have authenticated```
        </p>
    </p>
    <p>
        &ensp;&ensp;&ensp;**`await signout(password)`**
        <p>
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;This function is a *[coroutine](https://wiki.vg/Mojang_API#Get_list_of_questions "a coroutine")*.  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Invalidates an access token using an accounts username and password.  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;```Note: This requires the user to have authenticated```
        </p>
    </p>
    <p>
        &ensp;&ensp;&ensp;**`await invalidate()`**
        <p>
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;This function is a *[coroutine](https://wiki.vg/Mojang_API#Get_list_of_questions "a coroutine")*.  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Invalidates an access token using a client/access token pair.  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;```Note: This requires the user to have authenticated```
        </p>
    </p>
<br/><br/>
<br/><br/>

## Data Services
**`class MojangAPI.DataService.Data()`**
    <p>
        &ensp;&ensp;&ensp;Stores methods for getting information not related to a specific User.    
        &ensp;&ensp;&ensp;All of its methods are *[class methods](https://www.programiz.com/python-programming/methods/built-in/classmethod "Mojang API")*
    </p>
    <p>
        &ensp;&ensp;&ensp;**`await getBlockedServers`**
        <p>
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Returns a list of SHA1 hashes used to check server addresses against when the client tries to connect.  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;More information can be found [here](https://wiki.vg/Mojang_API#Blocked_Servers "Mojang API")
        </p>
    </p>
    <p>
        &ensp;&ensp;&ensp;**`await getStatistics(**kwargs)`**
        <p>
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Returns sale data corresponding to the sum of all the requested types.  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;The valid keyword arguments are:   
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;> item_sold_minecraft  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;> prepaid_card_redeemed_minecraft  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;> item_sold_cobalt  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;> item_sold_scrolls  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;> prepaid_card_redeemed_cobalt  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;> item_sold_dungeons  
        </p>
    </p>
    <p>
        &ensp;&ensp;&ensp;**`await checkServerStatus()`**
        <p>
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Returns a list of dictionaries containing the status of various Mojang services.  
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Possible values are `green` (no issues), `yellow` (some issues) and `red` (service unavailable).
        </p>
    </p>
    <p>
        &ensp;&ensp;&ensp;**`await getProfiles(*usernames)`**
        <p>
            &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Returns a list of usernames and their corresponding UUID's.  
        </p>
    </p>
 
