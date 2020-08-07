import { writable, Writable } from 'svelte/store';

export const  recordData: Writable<Array<number>> | null = writable(null);