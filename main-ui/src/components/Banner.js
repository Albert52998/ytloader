import {PureComponent} from 'react';
import './main.css';
import './fonts/fonts.css';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faArrowAltCircleDown} from '@fortawesome/free-solid-svg-icons';
// import CSRFToken from './csrftoken/csrftoken';
// import {NavLink} from 'react-router-dom';

export default class Banner extends PureComponent {
  // constructor() {
  //   super();
  //   this.state = {
  //     isComplete: false
  //   };
  // };
  //
  // componentDidMount() {
  //   fetch('/video/download/')
  //     .then(response => response.json())
  //     .then(json => this.setState({ isComplete: !this.state.isComplete }));
  // };

  render() {
    return (
        <div>
          <div className="banner">
            <div className="container">
              <div className="searchForm" id="search-form">
                <form className="banner__form" id="banner__form" method="POST" action="/video/download/">
                  {/* <CSRFToken /> */}
                  <div>
                    <input className="banner__input" id="banner__input" type="text" placeholder="Enter link" autocomplete="off" name='url' maxlength="100" />

                      <button type="submit" className="banner__btn" id="banner__btn">
                        {/*<NavLink to="/download-complete/" exact>*/}
                          <FontAwesomeIcon icon={faArrowAltCircleDown} size="3x" />
                        {/*</NavLink>*/}
                      </button>

                  </div>
                </form>

                <h1 id="loadingText">loading your video...</h1>
              </div>
            </div>
          </div>
        </div>
    );
  };
}