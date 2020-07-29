import { writable, Writable } from 'svelte/store'

export enum State {
    E = 0, O, X      // empty, O, X
}

export const gameLog : Writable<any[]> = writable([])      // stores the history of the gameplay

