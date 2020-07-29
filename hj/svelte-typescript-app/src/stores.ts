import { writable, Writable } from 'svelte/store'

enum State {
    E = 0, O, X      // empty, O, X
}

export const cells : Writable<State[][]> = writable([      // stores the current status of game board cells
    [State.E, State.E, State.E],
    [State.E, State.E, State.E],
    [State.E, State.E, State.E]
]);

export const gamePlay : Writable<any[]> = writable([])      // stores the history of the gameplay

