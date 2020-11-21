import {PureComponent} from 'react';
import './main.css';
import './fonts/fonts.css';
import {NavLink} from 'react-router-dom';

export default class Header extends PureComponent {

  render() {
    return (
        <div>
          <header className="header">
            <div className="container">
              <div>

                <NavLink
                    className="logo"
                    to="/"
                    exact
                >YTLoader</NavLink>

                <NavLink
                    className="help"
                    to="/help/"
                    exact
                >Help</NavLink>

              </div>
            </div>
          </header>
        </div>
    );
  };
}