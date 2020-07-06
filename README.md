# Mojang-API-Wrapper
## Overview
* Pythonic wrapper making use of `await` and `asnyc`
* 100% Coverage of Mojang's API and Authentication API

# Examples
### Accessing a players skin
```python
import ...
async def main():
    user = await User.createUser('Minecraft playername')
    profile = await user.getProfile()
    print(profile.skin) # Will print the skins URL

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```


### Changing a players skin
<details><summary>Note</summary>
<p>
Please note that Mojang's API may not trust your IP. To check if this is the case run the following code:

```python
import ...
async def main():
    user = await User.createUser('Minecraft playername')
    await user.authenticate('Mojang Email', 'Mojang password')
    await user.checkForSecurityQuestions() 
    # Will raise an error if untrusted
```

If your IP is untrusted you can complete security challenges to become trusted (I believe you only need to do this once). To get the security questions your Mojang account will need them active (refer to https://help.minecraft.net/hc/en-us/articles/360034686852-Resetting-Security-Questions). After which run `questions = await user.getSecurityQuestions()` to get the questions, and then `await user.sendSecurityAnswers(answers)` with the answers in the form refered to in the API's documentation (https://wiki.vg/Mojang_API#Send_back_the_answers).
</p>
</details>

```python
import ...
async def main():
    user = await User.createUser('Minecraft playername')
    await user.authenticate('Mojang Email', 'Mojang password')
    await user.changeSkin('Skin url', slim_model = True)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

### Getting sales data
```python
import ...
async def main():
    data = await DataService.getStatistics(prepaid_card_redeemed_minecraft=True)
    # Valid keyword arguments can be found at https://wiki.vg/Mojang_API#Payload_4
    print(data)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
