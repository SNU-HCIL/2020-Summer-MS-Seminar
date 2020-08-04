import { writable, Writable } from 'svelte/store'

export enum State {
    E = 0, O, X      // empty, O, X
}

export const gameLog : Writable<any[]> = writable([])      // stores the history of the gameplay
gameLog.set([
    {
        board: [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]],
        before_turn: State.X
    }
]); 

export const logStatus : Writable<number> = writable(0);

export const loginSuccessStore : Writable<boolean> = writable(false);

export const idStore : Writable<string> = writable("");


