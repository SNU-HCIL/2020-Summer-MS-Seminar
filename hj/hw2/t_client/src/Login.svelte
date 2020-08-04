<script lang="ts">
    import { loginSuccessStore, idStore } from './stores'
    import axios from 'axios'

    let domain = "http://localhost:8000/login/";

    let signInId : string;
    let signUpId : string;

    function checkInvalidId(id : string) : boolean {
        return ( id == "" ||
                 id == undefined ||
                 id.includes(' ') );
    }

    async function getToken() {
        await axios.get(domain, { withCredentials: true });
    }

    function getCookie(name: string): string {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    async function signIn() {
        if(checkInvalidId(signInId)) {
            alert("Wrong ID!!")
            signInId = "";
        }
        else {
            await getToken();
            const csrftoken : string = getCookie("csrftoken");
            const response = await axios.put(domain + "signin/", 
            {
                id: signInId,
            },
            {
                withCredentials: true,
                headers: {
                    "X-CSRFToken" : csrftoken
                },
            });
            // console.log(response)
            if(response.data.result) {
                alert("Sign in Succeed. Hello " + signInId);
                loginSuccessStore.set(true);
                idStore.set(signInId);
            }
            else {
                alert("Unregistered ID...");
            }
            signInId = "";
        }
    }

    async function signUp() {
        if(checkInvalidId(signUpId)) {
            alert("Input valid ID!!");
            signUpId = "";
        }
        else {
            await getToken();
            const csrftoken : string = getCookie("csrftoken");
            const response = await axios.post(domain + "signup/", 
            {
                id: signUpId,
            },
            {
                withCredentials: true,
                headers: {
                    "X-CSRFToken" : csrftoken
                },
            });
            console.log(response);
            alert(response.data);
            signUpId = "";
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
