import {writable, derived} from 'svelte/store'

export namespace GameStatManager{
    class GameInfo{
        start: Date
        end: Date
        length: number
        result: string

        constructor(start:string, end:string, length:number, result:string){
            this.start = new Date(start)
            this.end = new Date(end)
            this.length = length
            this.result = result
        }
    }

    class GameStats{
        games: Array<GameInfo> = new Array
        
        setRecords(games:Array<Object>){
            this.games = games.map(g => {
                return new GameInfo(
                    g['start'],
                    g['end'],
                    g['game_turns'],
                    g['result']
                )
            })
        }

        result(){
            return {
                win: this.games.filter(g => g['result'] == "WIN").length,
                lose: this.games.filter(g => g['result'] == "LOSE").length,
                draw: this.games.filter(g => g['result'] == "DRAW").length
            }
        }
    }
    
    function initializeGameStatsWritable(){
        const {subscribe, set, update} = writable(new GameStats)
        return{
            subscribe,
            updateRecord: (games: Array<Object>) => update(gs =>{gs.setRecords(games); return gs})
        }
    }

    export const gameStats = initializeGameStatsWritable()
    export const aggrGameResult = derived(gameStats, $gameStats => $gameStats.result())

}