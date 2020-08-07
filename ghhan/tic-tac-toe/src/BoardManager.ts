import {writable, derived} from 'svelte/store'
import type {BoardState} from './BoardState'

export namespace BoardManager{
    class GameHistory{
        history: Array<BoardState> = new Array;
        head: number = -1
    
        currentState(){
            return this.history[this.head]
        }
    
        push(state: BoardState){
            if(this.canRedo()){
                this.history.splice(this.head + 1)
            }
            
            this.head++
            this.history.push(state)
        }
    
        canUndo(){
            return this.head > 0
        }
    
        canRedo(){
            return this.head < this.history.length - 1
        }
    
        undo(){
            if(this.canUndo()){
                this.head--;
                console.log("now the head is :", this.head);
            }
        }
    
        redo(){
            if(this.canRedo()){
                this.head++;
                console.log("now the head is :", this.head);
            }
        }
    
        changeStateTo(current: number){
            if(current >=0 && current < this.history.length){
                this.head = current
                console.log("now the head is :", this.head);
            }
        }
    
    }
    
    function initializeHistoryWritable(){
        const {subscribe, set, update} = writable(new GameHistory)
        return{
            subscribe,
            push: (state: BoardState) => update(h => {h.push(state); return h}),
            undo: () => update(h => {h.undo(); return h}),
            redo: () => update(h => {h.redo(); return h}),
            changeStateTo: (current:number) => update(h => {h.changeStateTo(current); return h})
        }
    }
    
    export const gameHistory = initializeHistoryWritable()
    
    export const gameStatus = derived(
        gameHistory,
        $gameHistory => {
            const winConditions = [
                [0, 1, 2],
                [3, 4, 5],
                [6, 7, 8],
                [0, 3, 6],
                [1, 4, 7],
                [2, 5, 8],
                [0, 4, 8],
                [2, 4, 6],
            ];

            let boardState = $gameHistory.currentState();

            if(boardState !== undefined){
                
                for (let i = 0; i < winConditions.length; i++){
                    const [a, b, c] = winConditions[i]
                    if((boardState.cells[a] === boardState.cells[b]) && (boardState.cells[a] === boardState.cells[c])){
                        if(boardState.cells[a] != '')
                            return "Win"
                    }
                }

                if($gameHistory.head == 9){
                    return "Draw"             
                }

                return "Not Determined"
            }

            else{
                return "Not Determined";
            }
        }
    )

}