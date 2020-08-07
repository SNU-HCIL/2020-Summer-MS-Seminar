import {writable, derived} from 'svelte/store'

class Session{
    id:string = ''
    logged_in:boolean = false

    loggedIn(){
        return this.logged_in
    }
    setId(id:string){
        this.id = id
    }
    setLoggedIn(status:boolean){
        this.logged_in = status
    }
}

function initializeSessionWritable(){
    const {subscribe, set, update} = writable(new Session)
    return {
        subscribe,
        updateId: (id:string) => update(s => {s.setId(id); return s}),
        updateLoggedInStatus: (status:boolean) => update(s => {s.setLoggedIn(status); return s})
    }
}

export const sessionStatus = initializeSessionWritable()