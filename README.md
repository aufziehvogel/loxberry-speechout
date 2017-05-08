# loxberry-speechout
Loxberry plugin which allows you to have voice-out for your text messages from Loxone Mini Server

## Perform text-to-speech

```
/say?text=<text>&gain=<volume-adjustment>
```

Says the given text to speech-out with a volume adjustment. The volume
adjustment is a factor which will be added to the created sound file before
it is played. Thus, the base volume of your pi will remain the same, but the
text will appear louder. However, the quality goes down if the gain factor
is too high.

Example:

```
/say?text=Hello&gain=1.0
```
