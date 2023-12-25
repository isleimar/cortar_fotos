import cv2
import dlib

class Cut_photos:

    def __init__(self) -> None:        
        self.__width = 0
        self.__height = 0
        pass

    def _calculate_rectangle(self, image):                
        reason = self.reason
        old_height, old_width  = image.shape[:2]
        old_reason = old_width / old_height
        dx, dy = (0,0)
        x,y,new_width,new_height = (0,0,old_width,old_height)
        if old_reason != reason:            
            cx, cy = self._get_frontal_face(image)            
            if old_reason > reason:
                new_width = int(reason * old_height)
                half_width = int(new_width / 2)
                dx = cx - half_width
                dx = dx if dx > 0 else 0
                dx = dx if (dx + half_width) < old_width else old_width - new_width
                # cv2.line(image, (half_width +dx,0), (half_width +dx, old_height),(0,255,0),2)
                # print ("Dx: ", dx)
            else:
                new_height = int(old_width / reason)
                half_height = int(new_height / 2)
                dy = cy - half_height                
                dy = dy if dy > 0 else 0
                dy = dy if (dy + half_height) < old_height else old_height - new_height
                # cv2.line(image, (0, half_height +dy), (old_width, half_height +dy),(0,255,0),2)
                # print ("Dy: ", dy)
            
        return (x + dx,y + dy,new_width,new_height)
    
    def _get_frontal_face(self, image):
        detector_face = dlib.get_frontal_face_detector()
        faces_detected = detector_face(image, 1)
        if len(faces_detected) == 0:
            return (0,0)
        left, top, right, bottom = None,None,None,None
        for face in faces_detected:
            left = face.left() if (left is None or face.left() < left) else left
            top = face.top() if (top is None or face.top() < left) else top
            right = face.right() if (right is None or face.right() > right) else right
            bottom = face.bottom() if (bottom is None or face.bottom() > bottom) else bottom
        x, y = int((right + left) /2), int((bottom + top) /2) 
        # cv2.line(image, (x -2, y), (x +2, y), (0,0,255), 2)
        # cv2.line(image, (x, y -2), (x, y +2), (0,0,255), 2)
        return x, y
    
    @property
    def height(self) -> int:
        return self.__height
    @height.setter
    def height(self, value: int):
        self.__height = value
    
    @property
    def width(self) -> int:
        return self.__width
    @width.setter
    def width(self, value: int):
        self.__width = value

    @property
    def reason(self):
        return self.width / self.height
    
    def cut(self, input_photo, output_photo):
        image = cv2.imread(input_photo)        
        x,y, new_width, new_height = self._calculate_rectangle(image)
        new_image = image[y:y+new_height, x:x+new_width]
        cv2.imwrite(output_photo, new_image)
    

    



