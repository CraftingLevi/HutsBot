# HutsBot

To run, this requires the following folders and files to be added:
src/
src/config.JSON --> contains a JSON, content described below
src/themaselectie.mp3 --> sound file in mp3 format
src/welterusten.mp3 --> sound file in mp3 format

config.JSON should have the following form:
{
"token":"<DISCORD APPLICATION TOKEN>", 
"thema_users":"[<(int) UUID>...<(int) UUID>]",
"google_sheet_link":"<link to google sheet file>"
}

thema_users are the only ones allowed to roll a thema. The UUID of a users can be identified when running the bot, as user ids
are shown when users use commands. 
