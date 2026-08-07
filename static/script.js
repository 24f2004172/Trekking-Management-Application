var app = new Vue({
    el: "#app",
    data: {
        res_data: ""
    },
    methods: {
        load_trekker: function () {
            window.location.href = '/' + 'trekker';
        },
        load_admin: function () {
            window.location.href = '/' + 'admin';
        }
    },
})

var app_register = new Vue({
    el: "#register",
    data: {
        name: "",
        email: "",
        phone: "",
        password: "",
        responseMessage: ""
    },
    methods: {
        register_trekker: async function () {
            const url = 'http://127.0.0.1:5000/api/register';
            const payload = {
                name: this.name,
                email: this.email,
                phone: this.phone,
                password: this.password
            };

            try {
                const response = await fetch(url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(payload)
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }

                const data = await response.json();
                this.responseMessage = `${data.message}`;
            } catch (error) {
                this.responseMessage = `Error: ${error.message}`;
            }
        }
    }
})


var app_login = new Vue({
    el: '#login',
    data: {
        email: "",
        password: "",
        responseMessage: "",
        role: ""
    },
    methods: {
        login: async function(){
            const url = 'http://127.0.0.1:5000/api/login';
            const payload = {
                email: this.email,
                password: this.password
            };

            try {
                const response = await fetch(url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(payload)
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }

                const data = await response.json();
                this.responseMessage = `${data.message}`;
                // this.role = `${data.user["role"]}`
                // if(this.role === 'Trekker'){
                //     this.load_trekker()
                // }
                // if(this.role === 'Admin'){
                //     // this.load_admin()
                // }
            } catch (error) {
                this.responseMessage = `Error: ${error.message}`;
            }
        }
        // load_trekker: function () {
        //     window.location.href = '/' + 'trekker';
        // },
        // load_admin: function () {
        //     window.location.href = '/' + 'admin';
        // }
    }
})