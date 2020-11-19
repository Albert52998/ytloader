import React, { PureComponent } from 'react';
import { NavLink } from 'react-router-dom';

export default class Header extends PureComponent {

    render() {
        return (
            <div>
                <header className="header">
                    <div className="container">
                        <div>
                            <a className="logo" href="#0">YTLoader</a>
                            <a className="help" href="#0">Help</a>
                        </div>
                    </div>
                </header>
            </div>
        );
    };
}