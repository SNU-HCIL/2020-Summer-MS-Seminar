<script lang="ts">
    import { loginSuccessStore } from './stores'
    import axios from 'axios'

    let signInId : string;
    let signUpId : string;

    function checkInvalidId(id : string) : boolean {
        return ( id == "" ||
                 id == undefined ||
                 id.includes(' ') );
    }
    
    async function signIn() {
        if(checkInvalidId(signInId)) {
            alert("Wrong ID!!")
            signInId = "";
        }
        else {
            const response = await axios.get("http://localhost:8000/login/");
            alert("Welcome!!");
            console.log(response);
            loginSuccessStore.set(true);
        }
    }

    function signUp() {
        if(checkInvalidId(signUpId)) {
            alert("Input valid ID!!");
            signUpId = "";
        }
        else {
            alert("Registered!! Your ID is " + signUpId);
        }
    }



</script>

<div>
    <div>
        <input bind:value={signInId}>
        <button class="signin" on:click="{signIn}">Sign in</button>
    </div>
    <div>
        <input bind:value={signUpId}>
        <button class="signup" on:click="{signUp}">Sign up</button>
    </div>
    
</div>

<style>
    .signin {    
        margin: 3px;
        width: 100px;
        padding: auto;
        border: 0px;
        border-radius: 5px;
        background: #8ec0fa;
        text-align: center;
        color: rgba(0, 0, 0, 1);
        cursor: pointer;
    }

    .signup {
        margin: 3px;
        width: 100px;
        padding: auto;
        border: 0px;
        border-radius: 5px;
        background: #ff6f69;
        text-align: center;
        color: rgba(0, 0, 0, 1);
        cursor: pointer;
    }

</style>
