# scripts

### fk.sh
`fk.sh` is a bash wrapper for faketime. Accept hour offset, run command with spoofed system time.  
Usage: `./fk.sh <offset_hours> <command...>`  
Example: Set time +2 hours forward, then run whoami  `./fk.sh +2 whoami`
  
Get UTC time:  
- Linux `date -u`  
- Windows `[System.DateTime]::UtcNow`  
