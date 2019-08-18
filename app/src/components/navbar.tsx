import React from 'react';
import '../css/nav.scss'

class Navbar extends React.Component{
    render(){
        return(
            <div>
                <ul id  = "nav">
                    CUDA Image Manipulation Software
                    <li><a>Home</a></li>
                    <li><a>About</a></li>
                    <li><a>FAQ</a></li>
                    <li><a>Contacts</a></li>
                    <li><a>Dummy</a></li>
                </ul>
            </div>
        )
    }
}

export default Navbar
