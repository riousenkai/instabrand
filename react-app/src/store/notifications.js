import { Switch } from "react-router";

const GET_NOTIFICATIONS = "notifications/GET_NOTIFICATIONS";

const getNotifications = (notifications) => ({
  type: GET_NOTIFICATIONS,
  payload: notifications,
});

export const getUserNotif = () => async (dispatch) => {
    const res = await fetch('/api/notifications')
    const data = await res.json()

}

export default function reducer(state = {}, action) {
    switch(action.type) {
        case GET_NOTIFICATIONS:
            return {...state, notifications: action.payload.notifications}
    }
}
