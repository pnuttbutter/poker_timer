# poker_timer

It's a bit ropey, but it works.  Written in Python v2, no additional modules required outside of the standard set. 

On execution, the pk_config.json data is loaded into the Stopwatch object to set up players, player_seconds, base_seconds & blind levels.

Json schema is as below:

```json
{
	"base_seconds": 420
	, "player_seconds": 60
	, "players": 5
	, "levels":
	[
		{"level": 1, "small_blind":50, "big_blind":100}
		, {"level": 2, "small_blind":100, "big_blind":200}
		, {"level": 3, "small_blind":150, "big_blind":300}
		, {"level": 4, "small_blind":200, "big_blind":400}
		, {"level": 5, "small_blind":250, "big_blind":500}
		, {"level": 6, "small_blind":300, "big_blind":600}
		, {"level": 7, "small_blind":400, "big_blind":800}
		, {"level": 8, "small_blind":500, "big_blind":1000}
		, {"level": 9, "small_blind":700, "big_blind":1500}	
		, {"level": 10, "small_blind":1000, "big_blind":2000}
		, {"level": 11, "small_blind":2000, "big_blind":4000}
		, {"level": 12, "small_blind":4000, "big_blind":8000}
		, {"level": 13, "small_blind":8000, "big_blind":16000}
		, {"level": 14, "small_blind":16000, "big_blind":32000}
		, {"level": 15, "small_blind":32000, "big_blind":64000}

	]	
	, "tables" : 1
}
```

The duration of each level is calculated by multiplying the number of players by the player seconds and then adding the base seconds.  The duration is displayed next to the player count. 

Changing the number of players recalculates the level duration accordingly, however this change is only applied when the timer is started at the beginning of a level and not while a level is in progress.

On clicking on the 'Start' button, the timer counts down from the duration set at that point.  The start button label is changed to 'Pause', and will pause the timer on click.  The label is changed againg to 'Continue', and timer will recommence on click.

Once the timer hits zero, the timer stops and the blind level is set to the next level from the json config.  Clicking 'Start' commences the next blind level.
