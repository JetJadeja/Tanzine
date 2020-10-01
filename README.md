# TanzineLang
Tanzine is a new programming language written and interpreted in Python. It is able to utilize Python's standard libraries as well a libraries on the [Python Package Index](https://pypi.org/). Using Tanzine, you are able to acheive relative imports, however package installation is not yet completed. 

## Please join our Discord server for help or ways to get involved: https://discord.gg/4aWwGQ4

### Warning ⚠️
Tanzine is an extremely new language, so there is no installation process. We are currently working on an installer to add the **tanzine** command to your path. 
The Tanzine tutorial listed below also does not cover **everything**. The Tanzine core team is working on docs, and you can feel free to help too by opening a PR!

## Basics 📒
Tanzine's syntax is simple to understand. Each statement comes after a definitive, which will tell tanzine what type of statement you are making. A definitive looks something like this: `@DEFINITIVE@`.

Statements in Tanzine are similar to those in other languages. For example, math is the exact same (besides definitives)! Let's add two numbers! Type: `@MATH@ 5 + 2`. Since we do not display anything, nothing happens. So, let's assign a variable to the output of *5 + 2* and then display it in the console. 

To assign variables, we can use the VAR definitive (`@VAR@`) followed by the variable name. So we could do `@VAR@ num` (however that would display an error). Next we can write an equal symbol and then the statement that we are setting the variable to. 

So we can type: `@VAR@ num = @MATH@ 5 + 2`. And there you go! We have defined a variable!

Now to print this variable we need to use the `print` function. To run functions, we must use the RUN definitive (`@RUN@`) followed by the function and parameters. The syntax for a function is `(function,arg1,arg2,arg3)`. **Note the lack of spaces between the arguments**! To use variables as arguments, we need to use the `@` symbol followed by the variable name. So, our variable `num` would be `@num` in our function. We can type `@RUN@ (/print,@num)` to print *num* out. This will output `7`! Full code: 
```
@VAR@ num = @MATH@ 5 + 2
@RUN@ (/print,@num)
```
Full output:
```
7
```

**More basics are yet to come!**

## Capabilities
Here is a snippet of code showing Tanzine's capabilities:
```
@FUNC@ <fetchJSON> [@url] {
  @VAR@ request = @RUN@ (requests/get,@url)
  @VAR@ son = @RUN@ (@request.json)
  @RUN@ (/print,@son)
  @RETURN@
}

@VAR@ response = @RUN@ (<fetchJSON>,"http://crows.sh:9000/cosmosis/getChain")

@RUN@ (/print,@response)
```
This code defines a function called **fetchJSON** that takes in a URL. You can use the function to make a GET request to the URL.
This code will make a request to `http://crows.sh:9000/cosmosis/getChain` and return the JSONified outputed. 

## Quick Start Guide 📋
First, you must start an app using Tanzine start app. `tanzine startapp AppName`. If you do not specify an app name, Tanzine will create one called *TanzineApp*. We can just use the default app name. Type `tanzine startapp`.

Next, open your IDE of choice and open our *TanzineApp* directory. There should be a file called **main.tzn**. You can open this file and start making some changes!

### More Information ℹ️
The core code behind Tanzine was written in just 3 hours (we've added more features, though). **This means that the core Tanzine code isn't pretty, but development team is working on polishing the codebase, and you can help too by opening a PR or reporting issues!**

## Please join our Discord server for help or ways to get involved: https://discord.gg/4aWwGQ4
The server has a Discord bot (called Tater) allowing you to run Tanzine code directly in Discord, and see the output as a response message from the bot. 
- Mention the bot by typing `@Tater` for instructions!
- Whenever an error is not covered by Tanzine (and the parser crashes), the bot **will create an issue in this repository**!

# Dev Team 👨‍💻
The core dev team currently consists of:

[JetDeveloping](https://github.com/JetDeveloping)

[TransmissionsDev](https://github.com/TransmissionsDev)
