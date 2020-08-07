<script lang='ts'>
    import axios from 'axios'
    import {sessionStatus} from './SessionStatusManager'

    const url = 'http://127.0.0.1:8000/tic_tac_toe_app/'
    
    let id:string
    let pw:string

    const csrfToken = async function getCSRFToken(){
        const response = await axios.get(url, {withCredentials: true})
        console.log(response, document.cookie)
        const token = document.cookie.split(';').map(s => {
            let splitted = s.trim().split('=')
            return {
                name: splitted[0],
                value: splitted[1]
            }
        }).find(c => c.name == 'csrftoken')
        console.log(token)
        return token.value
    }();

    async function logIn(id:string, pw:string){
        const response = await axios.post(
            url + 'log_in/',
            {
                userID: id,
                password: pw
            },
            {
                withCredentials: true,
                headers:{
                    'X-CSRFToken': csrfToken
                }
            }
        )
        if(response.data.was_successful){
            sessionStatus.updateId(id)
            sessionStatus.updateLoggedInStatus(true)
            alert(response.data.message)
        }
        else{
            alert(response.data.message)
        }
    }

    async function logOut(id:string, pw:string){
        const response = await axios.post(
            url + 'log_out/',
            {},
            {
                withCredentials: true,
                headers:{
                    'X-CSRFToken': csrfToken
                }
            }
        )
        if(response.data.was_successful){
            sessionStatus.updateId('')
            sessionStatus.updateLoggedInStatus(false)
            alert(response.data.message)
        }
        else{
            alert(response.data.message)
        }
    }

</script>
<div>
    <input bind:value={id}>
    <input id='pw' type='password' bind:value={pw}>
    <button 
        class='login' 
        on:click={() => logIn(id, pw)}
    >Log in</button>
</div>