<template>
    <nav class="navbar is-dark ">
        <div class="navbar-brand ">
            <img src="@/assets/P.png" width="50" height="50px">
            <router-link to="/dashboard/games" class="navbar-item ">
                <strong>Phaneuf Scrabble Stats</strong>
            </router-link>
        </div>
        <div class="navbar-menu  is-active">
            <div class="navbar-end ">
                <div class="navbar-item ">
                    <div class="buttons ">
                        <template v-if="!$store.state.isAuthenticated">
                            <router-link to="/sign-up" class="button is-dark is-small"><strong>Sign Up</strong></router-link>
                            <router-link to="/log-in" class="button is-light is-small"><strong>Log in</strong></router-link>
                        </template>
                        <template v-else>
                            <router-link to="/dashboard/games" class="button is-dark is-small">Games</router-link>
                            <router-link to="/dashboard/addgame" class="button is-dark is-small">New Game</router-link>
                            <router-link to="/dashboard/players" class="button  is-dark is-small">Players</router-link>
                            <button @click="logout()" class="button is-dark is-small"> Log Out</button>
                        </template>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
    import axios from 'axios'
    export default { 
    name: 'NavBar',
    methods: {
        async logout() { 
            await axios
                .post('/api/v1/token/logout')
                .then(response => { 
                    console.log('Logged Out')
                })
                .catch(error => { 
                    console.log(JSON.stringify(error))
                })

            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem('token')
            this.$store.commit('removeToken')

            this.$router.push('/log-in')
        }
    }
}
</script>